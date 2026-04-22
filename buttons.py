from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup,
                           WebAppInfo
                           )

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Asosiy menu"), KeyboardButton(text="Yordam")],

        [KeyboardButton(text="Tillar"), KeyboardButton(text="FAQ savollar")],

        [KeyboardButton(text="Ro'yxatdan o'tish"), KeyboardButton(text="Bizning saytimiz", web_app=WebAppInfo(url="https://www.academia.edu/"))],

        [KeyboardButton(text="Joylashuv yuborish", request_location=True)]
    ],
    resize_keyboard=True
)

language_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿O'zbek tili"), KeyboardButton(text="🇬🇧English")],
        [KeyboardButton(text="🇷🇺Русскый язык")]
    ],
    resize_keyboard=True
)

catalog_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Elektrotexnika"),
            KeyboardButton(text="O'yinchoqlar")
        ],
        [
            KeyboardButton(text="Kiyim-kechak"),
            KeyboardButton(text="Perfume")
        ],
        [
            KeyboardButton(text="Oziq-ovqat"),
            KeyboardButton(text="Oyoq-kiyim")
        ]
    ], resize_keyboard=True
)

elektronic_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Samsung S25", callback_data="samsung"), InlineKeyboardButton(text="I-Phone 17 pro max", callback_data="iphone")],
        [InlineKeyboardButton(text="Xiaomi", callback_data="xiaomi"), InlineKeyboardButton(text="Honor X9D", callback_data="honor")],
        [InlineKeyboardButton(text="Boshqa mahsulotlar", web_app=WebAppInfo(url="https://www.samsung.com/uz_ru/smartphones/galaxy-s26-ultra/?page=home"))]
    ]
)


