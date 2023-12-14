from aiogram.enums.content_type import ContentType          
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
import asyncio
import logging
from modules import moderation

API_TOKEN = "6829581961:AAG-f_vRxgGA17l1Uw7mmmxtWsvF_A6wGB0"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
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