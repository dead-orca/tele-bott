"""Quick test script to verify bot setup"""
import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

async def test_bot():
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    
    if not token:
        print("❌ ERROR: BOT_TOKEN not found in .env file")
        return
    
    print(f"✅ Token loaded: {token[:15]}...")
    
    try:
        bot = Bot(token=token)
        info = await bot.get_me()
        print(f"✅ Bot connected successfully!")
        print(f"   Username: @{info.username}")
        print(f"   Name: {info.first_name}")
        print(f"   ID: {info.id}")
        print("\n✅ Your bot is ready! Try sending /start in Telegram.")
    except Exception as e:
        print(f"❌ ERROR connecting to bot: {e}")
        print("\nPossible issues:")
        print("1. Token is incorrect")
        print("2. No internet connection")
        print("3. Telegram API is down")

if __name__ == '__main__':
    asyncio.run(test_bot())






