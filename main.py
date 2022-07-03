import os
import telebot
from services import drivers,teams,calendargp

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('API_KEY')

@bot.message_handler(commands=['pilotos'])
def get_drivers(message):
    response=drivers.get_drivers_response()
    bot.reply_to(message,response)

@bot.message_handler(commands=['escuderias'])
def get_drivers(message):
    response=teams.get_teams_response()
    bot.reply_to(message,response)

@bot.message_handler(commands=['horario'])
def get_drivers(message):
   response = calendargp.get_next_gp_response()
   bot.reply_to(message,response)

bot.polling()

