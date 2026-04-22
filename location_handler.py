from aiogram import Router, F
from aiogram.types import Message
from geopy import Nominatim
from geopy.distance import geodesic


manzil = (38.27298214855289, 67.90661010628358,)
geo = Nominatim(user_agent="geobot")
location_router = Router()

@location_router.message(F.location)
async def get_location(message: Message):
    a = message.location.latitude
    b = message.location.longitude

    km = geodesic(manzil, (a, b)).kilometers
    metr = geodesic(manzil, (a, b)).meters
    miles = geodesic(manzil, (a, b)).miles

    address = geo.reverse((a, b), language="uz")

    await message.answer(f"Sizning koordinatangiz: {a, b}\n\nManzilingiz: {address}")
    await message.answer(f"Masofa: {km} km | {metr} metr | {miles} miles")
 
