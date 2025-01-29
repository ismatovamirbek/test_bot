from aiogram import types
from aiogram.dispatcher import FSMContext
from pyexpat.errors import messages

from inline_buttons import during_register, confirm_buttons  # Kurs tanlash va tasdiqlash tugmalari
from settings import dp, CHANNEL_ID, bot
from register import Register
from default_buttons import phone_button
from check_sub import check_subscription  # Importing the check_subscription function from check_sub.py

GROUP_ID = -1002320531230  # Guruh ID

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

    full_name = clean_markdown(full_name)
    await state.update_data(full_name=full_name)

    await message.answer("📱 Telefon raqamingizni yuboring:", reply_markup=phone_button)
    await state.set_state(Register.phone_number)

@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def contact_handler(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    phone = clean_markdown(phone)

    await state.update_data(phone=phone)

    # Kurs tanlash bosqichi
    await message.answer("📚 Qaysi yo‘nalishda o‘qimoqchisiz?", reply_markup=during_register)
    await state.set_state(Register.course)

@dp.callback_query_handler(lambda c: c.data in ["kiber", "front", "back-end", "design"], state=Register.course)
async def course_handler(callback_query: types.CallbackQuery, state: FSMContext):
    course_dict = {
        "kiber": "Kiber Xavfsizlik",
        "front": "Front-End Dasturlash",
        "back-end": "Back-End Dasturlash",
        "design": "Grafik Dizayn"
    }

    course = course_dict[callback_query.data]
    await state.update_data(course=course)

    await callback_query.message.answer("Ma'lumotlaringiz to'g'ri? Yuborishni xohlaysizmi?",
                                        reply_markup=confirm_buttons)
    await state.set_state(Register.confirmation)


@dp.callback_query_handler(lambda c: c.data in ["confirm_yes", "confirm_no"], state=Register.confirmation)
async def confirmation_handler(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "confirm_yes":
        data = await state.get_data()
        full_name = data["full_name"]
        phone = data["phone"]
        username = callback_query.from_user.username or "Mavjud emas"
        course = data["course"]

        user_info = (
            f"📝 Yangi ro‘yxatdan o‘tish:\n\n"
            f"👨‍💼 Ism: {full_name}\n"
            f"📞 Telefon: {phone}\n"
            f"👤 Username: @{username}\n"
            f"🆔 Foydalanuvchi ID: {callback_query.from_user.id}\n"
            f"📚 Kurs: {course}"
        )


        try:
            await bot.send_message(GROUP_ID, user_info, parse_mode="HTML")
            await bot.send_message(CHANNEL_ID, user_info, parse_mode="HTML")
            await callback_query.answer("✅ Rahmat! Ma'lumotlaringiz muvaffaqiyatli yuborildi.", show_alert=True)
        except Exception as e:
            await callback_query.answer("❌ Ma'lumotlarni yuborishda xatolik yuz berdi. Keyinroq urinib ko‘ring.",
                                        show_alert=True)
            print(f"Error sending message to group and channel: {e}")

        await state.finish()
    elif callback_query.data == "confirm_no":
        await callback_query.answer(
            "Ma'lumotlaringiz yuborilmadi. Ro'yxatdan o'tish uchun yana bir bor tugmani bosing.", show_alert=True)
        await state.finish()

@dp.callback_query_handler(text="register_course")
async def start_register(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    # Kanalga obuna bo'lishini tekshiramiz
    is_subscribed = await check_subscription(user_id)

    if not is_subscribed:
        # If the user is not subscribed, show an alert and send a message with the subscription link
        await call.answer("Iltimos, botdan foydalanish uchun kanalga obuna bo'ling.", show_alert=True)
        await call.message.answer("Obuna bo'lish uchun kanalimga kirib obuna bo'ling: [Kanalga Obuna Bo'lish](https://t.me/my_test_group7)", parse_mode=types.ParseMode.MARKDOWN)
        return

    # If the user is subscribed, continue the registration process
    await call.message.answer("Iltimos, ismingiz va familiyangizni kiriting:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Register.full_name)
