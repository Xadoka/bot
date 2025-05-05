# config/bot_config.py
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("No token provided. Set BOT_TOKEN environment variable.")

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
