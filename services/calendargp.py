from datetime import datetime
from pickle import TRUE
from urllib import response
from services import beautifulsoupparser
#import beautifulsoupparser
#Parse the HTML
soup = beautifulsoupparser.getsoup(beautifulsoupparser.calendarurl)

def getallgps():
    '''This Function returns a list of string with the GP ordered by 
    dates.
    '''
    parsedGps = soup.find_all('span', itemprop = 'name')
    gpList = list()

    for parsedGp in parsedGps:
        gpList.append(parsedGp.text)
    
    return gpList

def getgp(gpnumber):
    '''This Function returns the gp of the provided number
    +2 it is neccesary to add because of the way the GPS are stored on the HTML
    '''
    return getallgps()[gpnumber+2]

def getallschedules():
    '''This Function returns a list of string with all the time-schedule of the GPs
    ordered by date
    '''
    parseredSchedule = soup.find_all('dl', class_ = 'datos-cf1')
    schedulesList = list()

    for schedule in parseredSchedule:
        schedulesList.append(schedule.text)
    return schedulesList

def getschedule(gpnumber):
    '''This Function returns the schedules of the provided GP number
    '''
    return getallschedules()[gpnumber]

def getscheduleresponse(schedule):
    '''Introduce jum of line in the schedule so it's more displayable by the bot.
    '''
    response=""
    caps=positioncap(schedule) #Where we found a Cap letter we have to insert a \N

    #TO DO - Improve this code
    i=0
    for cap in caps:
        if(i<len(caps)-1):
            response+=schedule[caps[i]:caps[i+1]]
            response+="\n"
            i+=1

    return response

def getallenddates():
    '''This Function returns a list of string with the finalization dates of the GP
    '''
    parseredEndates = soup.find_all('meta', itemprop = 'endDate')
    endDateList = list()

    for endDate in parseredEndates:
        endDateList.append(endDate['content'])

    return endDateList

def getallenddatesformated():
    '''Converts all the endDates string format
    '''
    notFormattedList = getallenddates()
    formattedList = list()
    counter = 0
    for i in notFormattedList:
        formattedList.append(convertgptodate(notFormattedList[counter]))
        counter+=1
        
    return formattedList

def getcounternextgp():
    '''Function that will return the number of the following GP
    '''
    global counterGP
    counterGP = 0 
    listEndDates = getallenddatesformated()

    for nextDate in listEndDates:
        if(comparedates(nextDate) is not None):
            print("Counter at this moment is:"+str(counterGP))
            return counterGP #If gpdate is bigger than today, next GP is the next race
        counterGP+=1
                  
def comparedates(enddateGPstr):
    '''Function that compares if the date of the finalization of the GP is bigger than today 
    returns NONE GP is already gone
    returns endateGP if date is bigger than today
    '''
    today = datetime.today()
    #Transforms String enddateGP into date, in order to be able to compare it
    enddateGPdate = datetime.strptime(enddateGPstr, "%Y-%m-%d")

    if(enddateGPdate>today):
        return enddateGPdate

def convertgptodate(gpdate):
    '''Converts any string to a substring in date format (YY-MM-D).
    '''
    return gpdate.rpartition("T")[0]

def positioncap(str):
    '''Returns a list the position of the capital letter of the given string.
    '''
    stcounter=0
    numCaps=0
    positioncaplist = list()

    for i in str:
        if i.isupper():
            #print("esta letra es mayus")
            numCaps+=1
            positioncaplist.append(stcounter)
        
        stcounter+=1
             
    return positioncaplist

def getnextgpresponse():
    '''This Function returns the following GP with it's schedule as a string response.
    '''
    counterGP = getcounternextgp()
    response="Próximo Gran Premio de Fórmula 1"+"\n"
    response+="----------------------------------------------"+"\n"
    followingGPresponse = getgp(counterGP)
    followingGPSchedule = getschedule(counterGP)
    followingGPScheduleResponse = getscheduleresponse(followingGPSchedule)

    response+=followingGPresponse+"\n"+"\n"

    response+="Horarios:"+"\n"
    response+="----------------------------------------------"+"\n"
    response+=followingGPScheduleResponse
    return response