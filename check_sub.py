# check_sub.py
from settings import CHANNEL_ID
from settings import bot

async def check_subscription(user_id: int):
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        return False
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False
