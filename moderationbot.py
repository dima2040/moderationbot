import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram.enums.content_type import ContentType          
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

from modules import moderation


load_dotenv()

api_token = os.environ.get("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет!")


@dp.message(Command("test"))
async def send_test(message: types.Message):
    await message.reply("тестовая команда")


async def main():
    dp.include_router(moderation.router)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())