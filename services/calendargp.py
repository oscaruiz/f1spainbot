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
    parsed_gps = soup.find_all('span', itemprop = 'name')
    gp_list = list()

    for parsed_gp in parsed_gps:
        gp_list.append(parsed_gp.text)
    
    return gp_list

def get_gp(gpnumber):
    '''This Function returns the gp of the provided number
    +2 it is neccesary to add because of the way the GPS are stored in the HTML
    '''
    return get_all_gps()[gpnumber+2]

def get_all_schedules():
    '''This Function returns a list of string with all the time-schedule of the GPs
    ordered by date
    '''
    parsered_schedule = soup.find_all('dl', class_ = 'datos-cf1')
    schedules_list = list()

    for schedule in parsered_schedule:
        schedules_list.append(schedule.text)
    return schedules_list

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
    parsered_endates = soup.find_all('meta', itemprop = 'endDate')
    enddate_list = list()

    for enddate in parsered_endates:
        enddate_list.append(enddate['content'])

    return enddate_list

def get_all_enddates_formated():
    '''Converts all the endDates string format
    '''
    not_formatted_list = get_all_enddates()
    formatted_list = list()
    counter = 0

    for i in not_formatted_list:
        formatted_list.append(convert_gp_to_date(not_formatted_list[counter]))
        counter+=1
        
    return formatted_list

def get_enddate_formatted(gpnumber):
    '''This Function returns the enddate of the actualGP as a String
    '''
    return get_all_enddates_formated()[gpnumber]

def getcounternextgp():
    '''Function that will return the number of the following GP
    '''
    global countergp
    countergp = 0 
    enddates_list = get_all_enddates_formated()

    for next_enddate in enddates_list:
        if(compare_dates(next_enddate) is not None):
            return countergp # If gpdate is bigger than today, next GP is the next race
        countergp+=1
                  
def compare_dates(enddategp_str):
    '''Function that compares if the date of the finalization of the GP is bigger than today 
    returns NONE GP is already gone
    returns endateGP if date is bigger than today
    '''
    today_date = date.today()
    today_datetime = datetime(today_date.year, today_date.month, today_date.day)
    
    # Transforms String enddateGP into date, in order to be able to compare it
    enddategp_date = datetime.strptime(enddategp_str, "%Y-%m-%d")

    if(enddategp_date>=today_datetime):
        return enddategp_date

def convert_gp_to_date(gpdate):
    '''Converts any string to a substring in date format (YY-MM-D).
    '''
    return gpdate.rpartition("T")[0]

def position_caps(str):
    '''Returns a list the position of the capital letter of the given string.
    '''
    stcounter=0
    num_caps=0
    positioncap_list = list()

    for i in str:
        if i.isupper():
            num_caps+=1
            positioncap_list.append(stcounter)
        
        stcounter+=1
             
    return positioncap_list

def get_next_gp_response():
    '''This Function returns the following GP with it's schedule as a string response.
    '''
    countergp = getcounternextgp()
    response="Próximo Gran Premio de Fórmula 1"+"\n"
    response+="----------------------------------------------"+"\n"
    following_gp_response = get_gp(countergp)
    following_gp_schedule = get_schedule(countergp)
    following_gp_schedule_response = get_schedule_response(following_gp_schedule)

    response+=following_gp_response+"\n"+"\n"

    response+="Horarios:"+"\n"
    response+="----------------------------------------------"+"\n"
    response+=following_gp_schedule_response
    return response
