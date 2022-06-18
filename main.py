import os
import telebot
from services import drivers,teams,calendargp

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('API_KEY')

@bot.message_handler(commands=['pilotos'])
def get_drivers(message):
    response=drivers.getdriverresponse()
    bot.reply_to(message, response)

@bot.message_handler(commands=['escuderias'])
def get_drivers(message):
    response=teams.getteamsresponse()
    bot.reply_to(message, response)

@bot.message_handler(commands=['horario'])
def get_drivers(message):
   response = calendargp.getnextgpresponse()
   bot.reply_to(message, response)

bot.polling()
#bot.infinity_polling(True)