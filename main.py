from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('7451812537:AAHOHpRCSwdV6bpvt1uVYbU1o2xdEwBb0eI')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу',
                                          web_app=WebAppInfo(url='https://sergey5478.github.io/Telegram/')))
    await message.answer('Hello', reply_markup=markup)


# @dp.message_handler(content_types=['web_app_data'])
# async def web_app(message: types.Message):
#     res = json.loads(message.web_app_data.data)
#     await message.answer(f'{res["name"]}, {res["email"]}')


executor.start_polling(dp)
