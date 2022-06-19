from bs4 import BeautifulSoup
import requests
from datetime import date

# We always get the year of the season we are in
year=str(date.today().year) 

# URLs of the webs we want to scrap
driversurl='https://es.motorsport.com/f1/standings/'+year+'/'
teamurl=driversurl+'?type=Team'
calendarurl='https://www.motor.es/formula-1/calendario-'+year

def get_soup(url):
    '''Function to parse HTMLs
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    return soup