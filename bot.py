import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
API_TOKEN = BOT_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Salom, welcome to the bot!")
    
async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
    