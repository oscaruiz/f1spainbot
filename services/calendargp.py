from datetime import date, datetime
from pickle import TRUE
from urllib import response
from services import beautifulsoupparser

# Parse the HTML
soup = beautifulsoupparser.get_soup(beautifulsoupparser.calendarurl)

def get_all_gps():
    '''This Function returns a list of string with the GP ordered by 
    dates.
    '''
    parsedGps = soup.find_all('span', itemprop = 'name')
    gpList = list()

    for parsedGp in parsedGps:
        gpList.append(parsedGp.text)
    
    return gpList

def get_gp(gpnumber):
    '''This Function returns the gp of the provided number
    +2 it is neccesary to add because of the way the GPS are stored in the HTML
    '''
    return get_all_gps()[gpnumber+2]

def get_all_schedules():
    '''This Function returns a list of string with all the time-schedule of the GPs
    ordered by date
    '''
    parseredSchedule = soup.find_all('dl', class_ = 'datos-cf1')
    schedulesList = list()

    for schedule in parseredSchedule:
        schedulesList.append(schedule.text)
    return schedulesList

def get_schedule(gpnumber):
    '''This Function returns the schedules of the provided GP number
    '''
    return get_all_schedules()[gpnumber]

def get_schedule_response(schedule):
    '''Introduce jump of line in the schedule so it's more displayable by the bot.
    '''
    response=""
    caps=position_caps(schedule) # Where we found a Cap letter we have to insert a \N

    # TO DO - Improve this code
    i=0
    for cap in caps:
        if(i<len(caps)-1):
            response+=schedule[caps[i]:caps[i+1]]
            response+="\n"
            i+=1

    return response

def get_all_enddates():
    '''This Function returns a list of string with the finalization dates of the GP
    '''
    parseredEndates = soup.find_all('meta', itemprop = 'endDate')
    endDateList = list()

    for endDate in parseredEndates:
        endDateList.append(endDate['content'])

    return endDateList

def get_all_enddates_formated():
    '''Converts all the endDates string format
    '''
    notFormattedList = get_all_enddates()
    formattedList = list()
    counter = 0
    for i in notFormattedList:
        formattedList.append(convert_gp_to_date(notFormattedList[counter]))
        counter+=1
        
    return formattedList

def get_enddate_formatted(gpnumber):
    '''This Function returns the enddate of the actualGP as a String
    '''
    return get_all_enddates_formated()[gpnumber]

def getcounternextgp():
    '''Function that will return the number of the following GP
    '''
    global counterGP
    counterGP = 0 
    listEndDates = get_all_enddates_formated()

    for nextDate in listEndDates:
        if(compare_dates(nextDate) is not None):
            print("Counter at this moment is:"+str(counterGP))
            return counterGP # If gpdate is bigger than today, next GP is the next race
        counterGP+=1
                  
def compare_dates(enddateGPstr):
    '''Function that compares if the date of the finalization of the GP is bigger than today 
    returns NONE GP is already gone
    returns endateGP if date is bigger than today
    '''
    today_date = date.today()
    today_datetime = datetime(today_date.year, today_date.month, today_date.day)
    
    # Transforms String enddateGP into date, in order to be able to compare it
    enddateGPdate = datetime.strptime(enddateGPstr, "%Y-%m-%d")

    if(enddateGPdate>=today_datetime):
        return enddateGPdate

def convert_gp_to_date(gpdate):
    '''Converts any string to a substring in date format (YY-MM-D).
    '''
    return gpdate.rpartition("T")[0]

def position_caps(str):
    '''Returns a list the position of the capital letter of the given string.
    '''
    stcounter=0
    numCaps=0
    positioncaplist = list()

    for i in str:
        if i.isupper():
            numCaps+=1
            positioncaplist.append(stcounter)
        
        stcounter+=1
             
    return positioncaplist

def get_next_gp_response():
    '''This Function returns the following GP with it's schedule as a string response.
    '''
    counterGP = getcounternextgp()
    response="Próximo Gran Premio de Fórmula 1"+"\n"
    response+="----------------------------------------------"+"\n"
    followingGPresponse = get_gp(counterGP)
    followingGPSchedule = get_schedule(counterGP)
    followingGPScheduleResponse = get_schedule_response(followingGPSchedule)

    response+=followingGPresponse+"\n"+"\n"

    response+="Horarios:"+"\n"
    response+="----------------------------------------------"+"\n"
    response+=followingGPScheduleResponse
    return response
