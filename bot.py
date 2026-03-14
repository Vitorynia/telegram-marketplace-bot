from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🤖 Бот менеджера маркетплейсов запущен")

@dp.message_handler(commands=["sales"])
async def sales(message: types.Message):
    await message.answer("📦 Продажи сегодня: 12 540 ₽")

executor.start_polling(dp)
