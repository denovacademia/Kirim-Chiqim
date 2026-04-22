import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from buttons import catalog_button
from electronic_handler import e_router
from command_handler import c_router
from register import register_router
from location_handler import location_router

from aiogram.client.default import DefaultBotProperties

bottoken = ""


bot = Bot(bottoken, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

@dp.message(F.text == "Asosiy menu")
async def catalog_cmd(message: Message):
    await message.answer("Marhamat katalog", reply_markup=catalog_button)

@dp.message(F.text == "Yordam")
async def yordam_cmd(message: Message):
    await message.answer("Nima yordam kerak?")


dp.include_router(e_router)
dp.include_router(c_router)
dp.include_router(register_router)
dp.include_router(location_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot ishlayapti")
    asyncio.run(main())
