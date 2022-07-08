from services import beautifulsoupparser 

def get_soup_teams():
    '''This Function parses the HTML for the teams.
    '''
    soup = beautifulsoupparser.get_soup(beautifulsoupparser.teamurl)
    return soup

def get_teams():
    '''This Function returns a list of string with the F1 teams ordered by 
    their position in the F1 ranking.
    '''
    # We parse all the teams in the HTML
    soup = get_soup_teams()
    parsed_teams = soup.find_all('span', class_ = 'name')
    teams_list = list()

    # We get the name of the team
    for parsed_team in parsed_teams:
        teams_list.append(parsed_team.text)
    
    return teams_list

def get_teams_score():
    '''This Function returns a list of string with the points of the F1 teams ordered by 
    their position in the F1 ranking.
    '''

    # We parse all the drivers scores in the HTML
    soup = get_soup_teams()
    parsed_scores = soup.find_all('td', class_ = 'ms-table_cell ms-table_field--total_points')
    scores_list = list()

    for parsed_score in parsed_scores:
        scores_list.append(parsed_score.text)

    return scores_list

def get_teams_response():
    '''This Function returns a string response of the teams list with their score in  
    the F1 championship.
    '''
    response="Clasificación de escuderías - F1"+"\n"
    response+="----------------------------------------------"+"\n"
    teams = get_teams()
    teams_score = get_teams_score()
    
    i=0
    for team in teams:
        response+=str(i+1)+")"+team+"- "
        
        score=teams_score[i]
        if(score==""):
            response+="0"+"\n"
        else:
            response+=score+"\n"

        i+=1

    return response
  