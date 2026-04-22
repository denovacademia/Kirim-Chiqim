from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from buttons import start_menu, language_button

c_router = Router()

@c_router.message(Command('start'))
async def start_salom(message: Message):
    name = message.from_user.full_name
    id = message.from_user.id
    tg = message.from_user.username
    language = message.from_user.language_code
    text = f"""
Name: <b>{name}</b>
telegram: <i>@{tg}</i>
id: <code>{id}</code>
til: {language}
"""
    await message.answer(text ,reply_markup=start_menu)

@c_router.message(Command("help"))
async def help_yordam(message: Message):
    await message.answer("<i>Nima yordam kerak?</i>")
    
@c_router.message(Command('language'))
async def language_cmd(message: Message):
    await message.answer("<i>Tillar bo'limi</i>", reply_markup=language_button)

