from datetime import date, datetime
import os
import telebot
from services import drivers,teams,calendargp

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('API_KEY')

#Variables for the date that the functions were called last time 
date_pilotos=calendargp.get_enddate_formatted(calendargp.getcounternextgp())
date_escuderias=calendargp.get_enddate_formatted(calendargp.getcounternextgp())

response_pilotos=drivers.get_drivers_response()
response_escuderias=teams.get_teams_response()

@bot.message_handler(commands=['pilotos'])
def get_drivers(message):
    '''This Function asks the bot to retrieve the F1 drivers championship ordered by points.
    If it is the first time it's called after the new results of a GP, the results are loaded.
    '''
    global date_pilotos
    global response_pilotos

    if(compare_enddate_with_actual(date_pilotos)):
        bot.reply_to(message,response_pilotos)
    else:
        waiting="Un momento, déjame consultar el mundial de pilotos..."
        bot.reply_to(message,waiting)
        response=drivers.get_drivers_response()
        bot.reply_to(message,response)

        response_pilotos=response
        date_pilotos=calendargp.get_enddate_formatted(calendargp.getcounternextgp())
        
@bot.message_handler(commands=['escuderias'])
def get_teams(message):
    '''This Function asks the bot to retrieve the F1 teams championship ordered by points.
    If it is the first time it's called after the new results of a GP, the results are loaded.
    '''
    global date_escuderias
    global response_escuderias
    
    if(compare_enddate_with_actual(date_escuderias)):
        bot.reply_to(message,response_escuderias)
    else:
        waiting="Un momento, déjame consultar el mundial de escuderías..."
        bot.reply_to(message,waiting)
        response=teams.get_teams_response()
        bot.reply_to(message,response)

        response_escuderias=response
        date_escuderias=calendargp.get_enddate_formatted(calendargp.getcounternextgp())

@bot.message_handler(commands=['horario'])
def get_schedules(message):
    '''This Function asks the bot to retrieve the next GP with it's schedules.
    '''
    response = calendargp.get_next_gp_response()
    bot.reply_to(message,response)

def compare_enddate_with_actual(old_enddategp_str):
    '''Compares the parameter endDate with the next EndDate and returns true if it's the same. Also
    '''
    # Transforms String old_enddateGP into date, in order to be able to compare it
    old_enddategp_date = datetime.strptime(old_enddategp_str, "%Y-%m-%d")
    todays_enddate = datetime.strptime(calendargp.get_enddate_formatted(calendargp.getcounternextgp()),"%Y-%m-%d")
    today_date = date.today()
    today_datetime = datetime(today_date.year, today_date.month, today_date.day)

    if old_enddategp_date == todays_enddate and today_datetime != todays_enddate:
        return True



bot.polling()
