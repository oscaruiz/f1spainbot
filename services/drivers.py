from numpy import empty
from services import beautifulsoupparser

def get_soup_drivers():
    '''This Function parses the HTML for the drivers.
    '''
    soup = beautifulsoupparser.get_soup(beautifulsoupparser.driversurl)
    return soup

def get_drivers():
    '''This Function returns a list of string with the F1 drivers ordered by 
    their position in the F1 ranking.
    '''
    # We parse all the drivers in the HTML
    soup = get_soup_drivers()
    parsed_drivers = soup.find_all('span', class_ = 'name')
    drivers_list = list()

    # We get the name of the driver
    for parsed_driver in parsed_drivers:
        drivers_list.append(parsed_driver.text)

    return drivers_list

def get_drivers_score():
    '''This Function returns a list of string with the points of the F1 drivers ordered by 
    their position in the F1 ranking.
    '''

    # We parse all the drivers scores in the HTML
    soup = get_soup_drivers()
    parsed_scores = soup.find_all('td', class_ = 'ms-table_cell ms-table_field--total_points')
    scores_list = list()

    for parsed_score in parsed_scores:
        scores_list.append(parsed_score.text)

    return scores_list

def get_drivers_response():
    '''This Function returns a string response of the drivers list with their score in  
    the F1 championship.
    '''

    response="Clasificación de pilotos - F1"+"\n"
    response+="----------------------------------------------"+"\n"
    drivers = get_drivers()
    drivers_score = get_drivers_score()
    
    i=0
    for driver in drivers:
        response+=str(i+1)+")"+driver+"- "

        score=drivers_score[i]
        if(score==""):
            response+="0"+"\n"
        else:
            response+=score+"\n"

        i+=1

    return response
    