from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from settings import dp, bot
from register import Register
from default_buttons import phone_button

CHANNEL_ID = -1002295008102  # Kanal ID
GROUP_ID = -1002320531230    # Guruh ID

# Ha yoki Yo'q tugmalarini inline tarzda yaratish
confirm_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("✅ Ha", callback_data="confirm_yes")],
        [InlineKeyboardButton("❌ Yo'q", callback_data="confirm_no")]
    ]
)

# Markdown maxsus belgilarini tozalash funksiyasi
import re
def clean_markdown(text: str) -> str:
    return re.sub(r'([_*[\]()~`>#+\-=|{}.!])', r'\\\1', text)

@dp.message_handler(text="📝 Register")
async def start_register(message: types.Message, state: FSMContext):
    await message.answer("Iltimos, ismingiz va familiyangizni kiriting:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Register.full_name)

@dp.message_handler(state=Register.full_name)
async def full_name_handler(message: types.Message, state: FSMContext):
    full_name = message.text.strip()

    if len(full_name.split()) < 2:
        await message.answer("Iltimos, ism va familiyangizni to‘liq kiriting:")
        return

    # Markdown belgilarini tozalash
    full_name = clean_markdown(full_name)
    await state.update_data(full_name=full_name)
    # Telefon raqami kiritish uchun tugma
    await message.answer("📱 Telefon raqamingizni yuboring:", reply_markup=phone_button)
    await state.set_state(Register.phone_number)

@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def contact_handler(message: types.Message, state: FSMContext):
    # Agar foydalanuvchi telefon raqamini yuborsa (default button orqali)
    phone = message.contact.phone_number
    phone = clean_markdown(phone)  # Telefon raqamini tozalash

    await state.update_data(phone=phone)

    data = await state.get_data()
    full_name = data["full_name"]
    username = message.from_user.username or "Mavjud emas"

    # Xabarni tozalash va HTML formatida yuborish
    user_info = (
        f"📝 Yangi ro‘yxatdan o‘tish:\n\n"
        f"👨‍💼 Ism: {full_name}\n"
        f"📞 Telefon: {phone}\n"
        f"👤 Username: @{username}\n"
        f"🆔 Foydalanuvchi ID: {message.from_user.id}"
    )

    # Ma'lumotlarni tasdiqlash
    await message.answer("Ma'lumotlaringiz to'g'ri? Yuborishni xohlaysizmi?", reply_markup=confirm_buttons)
    await state.set_state(Register.confirmation)

@dp.callback_query_handler(lambda c: c.data in ["confirm_yes", "confirm_no"], state=Register.confirmation)
async def confirmation_handler(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "confirm_yes":
        # Foydalanuvchi tasdiqlasa, ma'lumotlarni yuborish
        data = await state.get_data()
        full_name = data["full_name"]
        phone = data["phone"]
        username = callback_query.from_user.username or "Mavjud emas"

        user_info = (
            f"📝 Yangi ro‘yxatdan o‘tish:\n\n"
            f"👨‍💼 Ism: {full_name}\n"
            f"📞 Telefon: {phone}\n"
            f"👤 Username: @{username}\n"
            f"🆔 Foydalanuvchi ID: {callback_query.from_user.id}"
        )

        try:
            # Xabarni HTML formatida yuborish
            await bot.send_message(GROUP_ID, user_info, parse_mode="HTML")
            await bot.send_message(CHANNEL_ID, user_info, parse_mode="HTML")
            await callback_query.answer("✅ Rahmat! Ma'lumotlaringiz muvaffaqiyatli yuborildi.",
                                        show_alert=True)
        except Exception as e:
            await callback_query.answer("❌ Ma'lumotlarni yuborishda xatolik yuz berdi. Keyinroq urinib ko‘ring.",
                                        show_alert=True)
            print(f"Error sending message to group and channel: {e}")

        await state.finish()

    elif callback_query.data == "confirm_no":
        # Agar foydalanuvchi "Yo'q" deb aytsa, ro'yxatdan o'tishni bekor qilish
        await callback_query.answer("Ma'lumotlaringiz yuborilmadi. Ro'yxatdan o'tish uchun yana bir bor tugmani bosing.",
                                    show_alert=True)
        await state.finish()
