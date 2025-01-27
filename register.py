from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    full_name = State()       # Foydalanuvchi ism va familiyasini kiritish
    phone_number = State()    # Foydalanuvchi telefon raqamini yuborish
    confirmation = State()    # Foydalanuvchi ma'lumotlarni tasdiqlash
