# f1spainbot
f1spainbot is a telegram bot made in Python that uses Beautifulsoup to retrieve information (Drivers/Teams Ranking and Next GP with schedules) of the current Formula-1 season.
The bot is thought for a a spanish audience, but the whole code is documented in english so don't be afraid to take a look at it if you don't speak spanish.

## Access the bot
To acces the bot, you just need to have a Telegram account.
Then, you can check it via the following link:
https://t.me/f1spain_bot

## Video Demo
If you don't have Telegram but you are curious about how the application works, here is a video that shows you:
https://www.youtube.com/watch?v=Sj_nGJKNbiw

## Why the bot uses BeautifulSoup instead of implementing an API?
After discovering Scrapy and Beautifulsoup in the Pluralsight's course 'Scraping your first web page with python' I thought about developing a small application to double-check what I learned. Then, I found out about some bots that were giving results about the F1 championship and I decided a challenge that was cool enough: implementing a bot that instead of using an API, uses web-parsing to retrieve results.

Also, I wanted to make the project public, because although I am little bit shy about the quality of my code I have used several free youtube, stackoverflow and free-internet content in my whole life. So it's my way of paying back the community, hopefully some of this code is usefull for someone :)

## Functions
The bot has three main functions that could be found in the 'main.py' file:

/pilotos

The spanish term for 'drivers'. It returns the ranking of F1 drivers ordered by points. The full logic of the service is implemented in services/drivers.py

/escuderias

The spanish term for 'teams'. It returns the ranking of F1 teams ordered by points. The full logic of the service is implemented in services/teams.py

/horario

The spanish term for 'schedules'. It returns the next GP based on the date that you are calling the function and it's schedules (FP,Q1,Q2,Race..)
The full logic of the service is implemented in services/calendargp.py and it's probably where the more interesting code of the application is.

Regarding BeautifulSoup,
NOTE: This bot doesn't have any commercial use, it's just for recreational/educational purposes.
The ranking of the F1 championship is parsed from: https://es.motorsport.com
and the calendar and schedules data are parsed  from: https://www.motor.es/

## Run the application

If you want to run the application locally, is as easy as having python installed an run the main.py:

python3 main.py

You may have to install telegram bot dependency the first time you run the bot, you can try with:
pip install pyTelegramBotAPI

## Environment variables
-API_KEY

Keep in mind that you will have to create a new Telegram Bot and set it as your API_KEY. 
