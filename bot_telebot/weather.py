import telebot
import requests
import json

bot = telebot.TeleBot('7451812537:AAHOHpRCSwdV6bpvt1uVYbU1o2xdEwBb0eI')
API = 'f295f1672735e334da89e93e2871695d'# С сайта о погоде


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Hello! Write down the name of your city')


@bot.message_handler(content_types=['text'])
def get_weather(message):
  city = message.text.strip().lower()
  res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
  if res.status_code == 200:
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    bot.reply_to(message, f'The weather is now: {temp}')

    image = 'Sun.jpg' if temp > 15.0 else 'Rain.jpg'
    file = open('./' + image, 'rb')
    bot.send_photo(message.chat.id, file)
  else:
    bot.reply_to(message, 'The city is specified incorrectly')


bot.polling(none_stop=True)
