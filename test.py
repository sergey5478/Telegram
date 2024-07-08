from aiogram import Bot, Dispatcher, executor, types
import json

API_TOKEN = '7451812537:AAHOHpRCSwdV6bpvt1uVYbU1o2xdEwBb0eI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', url='https://sergey5478.github.io/Telegram/'))
    await message.answer('Hello! Click the button to open the web page.', reply_markup=markup)

@dp.message_handler(content_types=['text'])  # Handle the purchase form data
async def process_web_app_data(message: types.Message):
    if message.text.startswith("order"):
        form_data = json.loads(message.text[5:])
        name = form_data.get("name", "No Name")
        email = form_data.get("email", "No Email")
        phone = form_data.get("phone", "No Phone")
        response = f"Thank you for your order!\nName: {name}\nEmail: {email}\nPhone: {phone}"
        await message.answer(response)

executor.start_polling(dp)
