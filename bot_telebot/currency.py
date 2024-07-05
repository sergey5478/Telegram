import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('7451812537:AAHOHpRCSwdV6bpvt1uVYbU1o2xdEwBb0eI')
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Hello! Enter the amount')
  bot.register_next_step_handler(message, get_amount)


def get_amount(message):
  global amount
  try:
    amount = int(message.text.strip())
  except:
    bot.send_message(message.chat.id, 'Введите число!')
    bot.register_next_step_handler(message, get_amount)
    return
  if amount > 0:
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
    btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
    btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
    btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Выберите пару валют!', reply_markup=markup)
  else:
    bot.send_message(message.chat.id, 'Введите положительное число!')
    bot.register_next_step_handler(message, get_amount)
    return


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  if call.data != 'else':
    values = call.data.upper().split('/')
    res = currency.convert(amount, values[0], values[1])
    bot.send_message(call.message.chat.id, f'Получилось: {round(res, 2)}. Пишите еще!')
    bot.register_next_step_handler(call.message, get_amount)
  else:
    bot.send_message(call.message.chat.id, 'Введите пару значений через /')
    bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
  try:
    values = message.text.upper().split('/')
    res = currency.convert(amount, values[0], values[1])
    bot.send_message(message.chat.id, f'Получилось: {round(res, 2)}. Пишите еще!')
    bot.register_next_step_handler(message, get_amount)
  except Exception:
    bot.send_message(message.chat.id, 'Введите пару значений через /')
    bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)
