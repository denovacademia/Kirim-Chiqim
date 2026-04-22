from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from buttons import elektronic_button

e_router = Router()

@e_router.message(F.text == "Elektrotexnika")
async def Elektrotexnika_cmd(mesage: Message):
    rasm_path = "elektrotexnika.jpg"
    rasm = FSInputFile(rasm_path)

    await mesage.answer_photo(rasm, caption="Marhamat Elektrotexnika bo'limi", reply_markup=elektronic_button)

# @e_router.message()
