from numpy import empty
from services import beautifulsoupparser

# Parse the whole HTML
soup = beautifulsoupparser.get_soup(beautifulsoupparser.driversurl)

def get_drivers():
    '''This Function returns a list of string with the F1 drivers ordered by 
    their position in the F1 ranking.
    '''
    # We parse all the drivers in the HTML
    parsedDrivers = soup.find_all('span', class_ = 'name')
    driversList = list()

    # We get the name of the driver
    for parsedDriver in parsedDrivers:
        driversList.append(parsedDriver.text)

    return driversList

def get_drivers_score():
    '''This Function returns a list of string with the points of the F1 drivers ordered by 
    their position in the F1 ranking.
    '''

    # We parse all the drivers scores in the HTML
    parsedScores = soup.find_all('td', class_ = 'ms-table_cell ms-table_field--total_points')
    scoresList = list()

    for parsedScore in parsedScores:
        scoresList.append(parsedScore.text)

    return scoresList

def get_drivers_response():
    '''This Function returns a string response of the drivers list with their score in  
    the F1 championship.
    '''

    response="Clasificación de pilotos - F1"+"\n"
    response+="----------------------------------------------"+"\n"
    drivers = get_drivers()
    driverScore = get_drivers_score()
    
    i=0
    for driver in drivers:
        response+=str(i+1)+")"+driver+"- "

        if(driverScore[i]==""):
            response+="0"+"\n"
        else:
            response+=driverScore[i]+"\n"

        i+=1

    return response