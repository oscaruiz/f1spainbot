from datetime import date, datetime
import os
from pickle import TRUE
import telebot
from services import drivers,teams,calendargp

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('API_KEY')

#Variables for the date that the functions were called last time 
datePilotos=calendargp.get_enddate_formatted(calendargp.getcounternextgp())
dateEscuderias=calendargp.get_enddate_formatted(calendargp.getcounternextgp())

responsePilotos=drivers.get_drivers_response()
responseEscuderias=teams.get_teams_response()

@bot.message_handler(commands=['pilotos'])
def get_drivers(message):
    '''This Function ask the bot to retrieve the F1 drivers championship ordered by points.
    If it is the first time it's called after the new results of a GP, the results are loaded.
    '''
    global datePilotos
    global responsePilotos

    if(compare_enddate_withActual(datePilotos)):
        bot.reply_to(message,responsePilotos)
    else:
        waiting="Un momento, déjame consultar el mundial de pilotos..."
        bot.reply_to(message,waiting)
        response=drivers.get_drivers_response()
        bot.reply_to(message,response)

        responsePilotos=response
        datePilotos=calendargp.get_enddate_formatted(calendargp.getcounternextgp())
        
@bot.message_handler(commands=['escuderias'])
def get_teams(message):
    '''This Function ask the bot to retrieve the F1 teams championship ordered by points.
    If it is the first time it's called after the new results of a GP, the results are loaded.
    '''
    global dateEscuderias
    global responseEscuderias
    
    if(compare_enddate_withActual(dateEscuderias)):
        bot.reply_to(message,responseEscuderias)
    else:
        waiting="Un momento, déjame consultar el mundial de pilotos..."
        bot.reply_to(message,waiting)
        response=teams.get_teams_response()
        bot.reply_to(message,response)

        responseEscuderias=response
        dateEscuderias=calendargp.get_enddate_formatted(calendargp.getcounternextgp())

@bot.message_handler(commands=['horario'])
def get_schedules(message):
    '''This Function ask the bot to retrieve the next GP with it's schedules.
    '''
    response = calendargp.get_next_gp_response()
    bot.reply_to(message,response)

def compare_enddate_withActual(oldEnddateGPstr):
    '''Compares the paramete endDate with the next EndDate and returns true if it's the same. Also
    '''
    # Transforms String old_enddateGP into date, in order to be able to compare it
    oldEnddateGPdate = datetime.strptime(oldEnddateGPstr, "%Y-%m-%d")
    todaysEnddate = datetime.strptime(calendargp.get_enddate_formatted(calendargp.getcounternextgp()),"%Y-%m-%d")
    today_date = date.today()
    today_datetime = datetime(today_date.year, today_date.month, today_date.day)

    if oldEnddateGPdate == todaysEnddate and today_datetime != todaysEnddate:
        return TRUE

bot.polling()
