from aiogram import Router, F, Bot
from aiogram.types import Message

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

bottoken = "8507992376:AAE0g4xa7kjbQsrQq3xRnM_SYimioeZeF34"
bot = Bot(bottoken)
register_router = Router()

admin = 6150566915

class Registerstate(StatesGroup):
    full_name = State()
    Date_of_Birth = State()
    phone_number = State()
    age = State()
    address = State()
    

@register_router.message(F.text == "Ro'yxatdan o'tish") 
async def start_register(message: Message,state: FSMContext):
        await message.answer("Ismingizni Kiriting")
        await state.set_state(Registerstate.full_name)

@register_router.message(Registerstate.full_name)
async def get_name(message: Message, state: FSMContext):
      await state.update_data(full_name=message.text)
      await message.answer("Tugilgan Kuningizni Kiriting")
      await state.set_state(Registerstate.Date_of_Birth)

@register_router.message(Registerstate.Date_of_Birth)
async def get_Date_of_Birth(message: Message, state: FSMContext):
      await state.update_data(Date_of_Birth=message.text) 
      await message.answer("Telefon RAqamingizni Kiriting")
      await state.set_state(Registerstate.phone_number)  

@register_router.message(Registerstate.phone_number) 
async def  get_phone_number(message: Message, state: FSMContext):
      await state.update_data(phone_number=message.text)
      await message.answer("Manzilingizni Kiriting")
      await state.set_state(Registerstate.address)


@register_router.message(Registerstate.address)
async def get_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Tabriklayaman Ro'yxatdan O'tdingiz ")
    data = await state.get_data()
    text = f"""
Yangi foydalanuvchi

Ism-familya: {data.get("full_name")}
Tug'ilgan sanasi: {data.get("Date_of_Birth")}
Telefon raqami: {data.get("phone_number")}
Yoshi: {data.get("age")}
Manzili: {data.get("address")}
"""
    await bot.send_message(admin, text)
