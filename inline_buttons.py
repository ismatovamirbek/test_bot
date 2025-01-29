from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

about_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Courses", callback_data="courses"),
            InlineKeyboardButton(text="🧑‍💻 Mentorlar", callback_data="mentors")
        ],
        [
            InlineKeyboardButton(text="Statistika", callback_data="statistics"),
            InlineKeyboardButton(text="Yangiliklar", callback_data="news")
        ]
    ]
)


back_to_about = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Back", callback_data="about_back")
        ]
    ]
)


our_mentors = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Abdumalikovich Rustamjon Isroilov", callback_data="abruis_dev"),
            InlineKeyboardButton(text="Otajon Bozorboyev", callback_data="otajon_dev")
        ]
    ]
)



social_media = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url="https://t.me/tramplin_uz"),
            InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/tramplinuz/")
        ],
        [
            InlineKeyboardButton(text="Web saxifa", url="https://www.tramplin.uz/")
        ],
        [
            InlineKeyboardButton(text="↩️ Back", callback_data="about_back")
        ]
    ]
)



our_courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kiber Xavfsizlik", callback_data="cuber_security"),
            InlineKeyboardButton(text="Front-End Dasturlash", callback_data="front-end")
        ],
        [
            InlineKeyboardButton(text="Back-End Dasturlash", callback_data="back-end"),
            InlineKeyboardButton(text="Grafik Dizayn", callback_data="graphic-designing")
        ],
        [
            InlineKeyboardButton(text="↩️ Back", callback_data="about_back")
        ]
    ]
)



# Ro‘yxatdan o‘tish tugmasi
register_course = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="register_course")
        ],
        [
            InlineKeyboardButton(text="↩️ Back", callback_data="about_back")
        ]
    ]
)


# Ha yoki Yo'q tugmalarini inline tarzda yaratish
confirm_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("✅ Ha", callback_data="confirm_yes")],
        [InlineKeyboardButton("❌ Yo'q", callback_data="confirm_no")]
    ]
)


during_register = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kiber Xavfsizlik", callback_data="kiber"),
            InlineKeyboardButton(text="Front-End Dasturlash", callback_data="front")
        ],
        [
            InlineKeyboardButton(text="Back-End Dasturlash", callback_data='back-end'),
            InlineKeyboardButton(text="Grafik Dizayn", callback_data="design")
        ]
    ]
)



