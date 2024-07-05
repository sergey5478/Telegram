from aiogram import Bot, Dispatcher, executor, types

bot = Bot('7451812537:AAHOHpRCSwdV6bpvt1uVYbU1o2xdEwBb0eI')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['photo']) # commands=['start']
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, "Hello!")
    # await message.answer('Hello!')
    await message.reply('Hello!')
    # file = open('/some.png', 'rb')
    # await message.answer_photo(file)


@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton('Site', url='https://ya.ru'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.reply('Hello!', reply_markup=markup)


executor.start_polling(dp)



