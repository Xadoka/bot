# main.py
import logging
from aiogram import executor
from config.bot_config import dp
from handlers import common, candidate, callback

# Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# Register handlers
common.register_handlers(dp)
candidate.register_handlers(dp)
callback.register_handlers(dp)


if __name__ == '__main__':
    logging.info("Starting Izbasar bot")
    executor.start_polling(dp, skip_updates=True)