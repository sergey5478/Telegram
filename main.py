from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7451812537:AAHOHpRCSwdV6bpvt1uVYbU1o2xdEwBb0eI')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу',
                                          web_app=WebAppInfo(url='https://sergey5478.github.io/Telegram/')))
    await message.reply('Hello', reply_markup=markup)


executor.start_polling(dp)



