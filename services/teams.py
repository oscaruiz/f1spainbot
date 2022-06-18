from services import beautifulsoupparser 
#Parse the HTML
soup = beautifulsoupparser.getsoup(beautifulsoupparser.teamurl)

def getteams():
    '''This Function returns a list of string with the F1 teams ordered by 
    their position in the F1 ranking.
    '''
    #We parse all the teams in the HTML
    parsedTeams = soup.find_all('span', class_ = 'name')
    teamsList = list()

    #We get the name of the team
    for parsedTeam in parsedTeams:
        teamsList.append(parsedTeam.text)
    
    return teamsList

def getteamsscore():
    '''This Function returns a list of string with the points of the F1 teams ordered by 
    their position in the F1 ranking.
    '''

    #We parse all the drivers scores in the HTML
    parsedScores = soup.find_all('td', class_ = 'ms-table_cell ms-table_field--total_points')
    scoresList = list()

    for parsedScore in parsedScores:
        scoresList.append(parsedScore.text)

    return scoresList

def getteamsresponse():
    '''This Function returns a string response of the teams list with their score in  
    the F1 championship.
    '''
    response="Clasificación de escuderías - F1"+"\n"
    response+="----------------------------------------------"+"\n"
    teams = getteams()
    teamsScore = getteamsscore()
    
    i=0
    for team in teams:
        response+=str(i+1)+")"+team+"- "
        
        if(teamsScore[i]==""):
            response+="0"+"\n"
        else:
            response+=teamsScore[i]+"\n"

        i+=1

    return response