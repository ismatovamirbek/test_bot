from settings import dp
from aiogram import types, executor
from default_buttons import start_button
from inline_buttons import *
from register_handler import *


# Start bot
@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!", reply_markup=start_button)



# About course
@dp.message_handler(text="ℹ️ About")
async def about_my_bot(message: types.Message):
    text = """Tramplin IT Akademiyasi zamonaviy kasblardan bir bo'lgan dasturlash sohasining turli yo'nalishlarida amaliyotga asoslangan metodikaasosida o'quvchilarga ta'lim beradi"""
    img = open("static/images/about_tramplin.jpg", "rb")
    await message.answer_photo(photo=img, caption=text, reply_markup=about_bot)


# Social Media
@dp.message_handler(text="📲 Social media")
async def our_media(message: types.Message):
    img = open("static/images/social_media.jpg", "rb")
    text = "Bizning ijtimoiy saxifalarimiz👇"
    await message.answer_photo(photo=img, caption=text, reply_markup=social_media)



# Mentors
@dp.callback_query_handler(text="mentors")
async def about_mentors(call: types.CallbackQuery):
    await call.message.delete()
    img = open("static/images/mentors.png", "rb")
    text = "Bizning malakali mentorlarimiz👇"
    await call.message.answer_photo(photo=img, caption=text , reply_markup=our_mentors)


# Abruis Dev
@dp.callback_query_handler(text="abruis_dev")
async def abruis_coder(call: types.CallbackQuery):
    await call.message.delete()
    text = """❇️ Python | Telegram bot | Web site
💻 Dars o’tish bo’yicha 3 yilik tajriba (250 dan oshiq shogirdlar)
Kursga ro’yxatdan o’tish ⬇️
https://t.me/abruisbot"""
    img = open("static/images/abruis_coder.jpg", "rb")
    await call.message.answer_photo(photo=img, caption=text, reply_markup=back_to_about)



# Otajon Developer
@dp.callback_query_handler(text="otajon_dev")
async def otajon_coder(call: types.CallbackQuery):
    text = "Full Stack developer, Data Science & AI developer, Python backend mentor."
    img = open("static/images/otajon_coder.jpg", "rb")
    await call.message.answer_photo(photo=img, caption=text, reply_markup=back_to_about)



# Statistics
@dp.callback_query_handler(text="statistics")
async def about_statistics(call: types.CallbackQuery):
    await call.message.delete()
    text = """Malakali mentorlar - 12+
Bitiruvchi - 250+
O'rtacha maosh - 300$
Ishga joylashish - 79%

Hozirda o’quvchilarimiz ko’rsatayotgan natijalar bizning maqsadimizga barqaror yaqinlashayotganimizning yaqqol isbotidir!"""
    await call.message.answer(text, reply_markup=back_to_about)



# Back to About
@dp.callback_query_handler(text="about_back")
async def back_to_my_about(call: types.CallbackQuery):
    await call.message.delete()
    text = """Tramplin IT Akademiyasi zamonaviy kasblardan bir bo'lgan dasturlash sohasining turli yo'nalishlarida amaliyotga asoslangan metodikaasosida o'quvchilarga ta'lim beradi"""
    img = open("static/images/about_tramplin.jpg", "rb")
    await call.message.answer_photo(photo=img, caption=text, reply_markup=about_bot)




# News
@dp.callback_query_handler(text="news")
async def about_news(call: types.CallbackQuery):
    await call.message.delete()
    vid = open("static/video/our_news.MP4", "rb")
    text = " Uchish vaqti keldi, bugun,hozir!"
    await call.message.answer_video(caption=text, video=vid, reply_markup=back_to_about)



# About Courses
@dp.callback_query_handler(text="courses")
async def about_our_courses(call: types.CallbackQuery):
    await call.message.delete()
    img = open("static/images/courses.jpg", "rb")
    text = "Bizning kurslarimiz"
    await call.message.answer_photo(photo=img, caption=text, reply_markup=our_courses)



# Cybersecurity
@dp.callback_query_handler(text="cuber_security")
async def our_cuber_security_course(call: types.CallbackQuery):
    await call.message.delete()
    text = "Ma'lumot: \nDarslar soni: 92 ta\nKurs davomiyligi: 8 oy\nMentor: John Johns\nReal loyiha: 4ta\nKurs narxi: 1800000 UZS\nAloqa yoki savollar uchun: +99895 106 36 00"
    img = open("static/images/during_course.jpg", "rb")
    await call.message.answer_photo(photo=img, caption=text, reply_markup=register)



# Front-End
@dp.callback_query_handler(text="front-end")
async def our_front_end_course(call: types.CallbackQuery):
    await call.message.delete()
    text = "Ma'lumot: \nDarslar soni: 90 ta\nKurs davomiyligi: 8 oy\nMentor: John Johns\nReal loyiha: 3ta\nKurs narxi: 1500000 UZS\nAloqa yoki savollar uchun: +99895 106 36 00"
    img = open("static/images/during_course.jpg", "rb")
    await call.message.answer_photo(photo=img, caption=text, reply_markup=register)




# Back-End
@dp.callback_query_handler(text="back-end")
async def our_back_end_course(call: types.CallbackQuery):
    await call.message.delete()
    text = "Ma'lumot: \nDarslar soni: 92 ta\nKurs davomiyligi: 8 oy\nMentor: John Johns\nReal loyiha: 2ta\nKurs narxi: 1500000 UZS\nAloqa yoki savollar uchun: +99895 106 36 00"
    img = open("static/images/during_course.jpg", "rb")
    await call.message.answer_photo(photo=img, caption=text, reply_markup=register)


# Graphic Designing
@dp.callback_query_handler(text="graphic-designing")
async def our_graphic_designing_course(call: types.CallbackQuery):
    text = "Ma'lumot: \nDarslar soni: 46 ta\nKurs davomiyligi: 4 oy\nMentor: John Johns\nReal loyiha: 5ta\nKurs narxi: 1500000 UZS\nAloqa yoki savollar uchun: +99895 106 36 00"
    img = open("static/images/during_course.jpg", "rb")
    await call.message.answer_photo(photo=img, caption=text, reply_markup=register)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
