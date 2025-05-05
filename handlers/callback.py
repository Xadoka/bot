from aiogram import Dispatcher, types
from config.bot_config import bot
import content.messages_ru as msgs_ru
import content.messages_kz as msgs_kz
from keyboards.reply_keyboards import get_candidate_menu_keyboard
import logging
# Import user language dictionary
from handlers.common import user_languages

async def process_faq_callback(callback_query: types.CallbackQuery):
    """Process FAQ callback queries"""
    logging.info("+++ Entered process_faq_callback +++")

    user_id = callback_query.from_user.id
    logging.info(f"User ID: {user_id}")
    data = callback_query.data
    lang = user_languages.get(user_id, "ru")
    logging.info(f"User language: {lang}")
    msgs = msgs_ru if lang == "ru" else msgs_kz

    try:
        if data in msgs.FAQ:
            logging.info(f"Sending FAQ answer to user {user_id}: {msgs.FAQ[data]}")
            await callback_query.message.answer(msgs.FAQ[data])
        else:
            logging.warning(f"Unknown FAQ callback data received: {data}")
            await callback_query.answer("Неизвестная команда.", show_alert=True)
    except Exception as e:
        logging.error(f"Error processing callback: {e}")
        await callback_query.answer("Произошла ошибка.", show_alert=True)
    finally:
        # Ensure callback is always answered
        await callback_query.answer()


def register_handlers(dp: Dispatcher):
    """Register callback handlers"""
    dp.register_callback_query_handler(
        process_faq_callback,
        lambda c: c.data.startswith("faq_")
    )