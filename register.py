from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    full_name = State()
    phone_number = State()
    course = State()  # <== BU YANGI QO'SHILGAN QATOR
    confirmation = State()
