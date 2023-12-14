from aiogram.enums.content_type import ContentType
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, F

router = Router()

forbidden_words = [
    "яблоко", "бот"
]

forbidden_word_parts = [
    "лох", "ш"
]

forbidden_word_parts_2 = [
    "о", "т"
]

@router.message(Command("word"))
async def add_bad_word(message: Message):
    word = message.text.split(' ')[1]
    forbidden_words.append(word)

@router.message(F.content_type != ContentType.TEXT)
async def no_image_handler(message: Message):
    # await bot.ban_chat_member(message.chat.id, message.from_user.id)
    await message.delete()

@router.message()
async def no_forbidden_words_handler(message: Message):
    text_array = message.text.split(' ')

    for item in text_array:
        for word in forbidden_words:
            if word.lower() == item.lower():
                await message.delete()
                return

        for part in forbidden_word_parts:
            if item.lower().startswith(part.lower()):
                await message.delete()
                return

        for part in forbidden_word_parts_2:
            if part.lower() in item.lower():
                await message.delete()
                return