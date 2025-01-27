from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("ℹ️ About"),
            KeyboardButton("📝 Register")
        ],
        [
            KeyboardButton("📲 Social media")
        ]
    ],
    resize_keyboard=True
)



phone_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📱 Raqamni yuborish", request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True
)
