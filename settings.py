from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


BOT_TOKEN = "8028920258:AAHRsF81t43McbtA5S1IKNUJKLAhJGAZn-M"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

