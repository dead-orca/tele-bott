"""Simple bot runner with error handling"""
import os
import sys
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable detailed logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

try:
    # Check token
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN not found!")
        print("Make sure .env file exists with: BOT_TOKEN=your_token")
        sys.exit(1)
    
    print(f"✅ Token loaded: {BOT_TOKEN[:15]}...")
    print("✅ Starting bot...")
    print("=" * 50)
    
    # Import and run bot
    from telegram.ext import Application
    from bot import main
    
    # Run the bot
    main()
    
except KeyboardInterrupt:
    print("\n\n⚠️ Bot stopped by user (Ctrl+C)")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    input("\nPress Enter to exit...")






