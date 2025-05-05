# handlers/common.py
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from config.bot_config import bot
from utils.states import BotStates
from keyboards.reply_keyboards import get_language_keyboard, get_main_menu_keyboard
import content.messages_ru as msgs_ru
import content.messages_kz as msgs_kz

# Dictionary to store user language preferences
user_languages = {}

async def cmd_start(message: types.Message):
    """Handler for /start command"""
    # Send welcome message
    await message.answer(msgs_ru.WELCOME_MESSAGE)
    
    # Show language selection keyboard
    await message.answer(
        msgs_ru.LANGUAGE_SELECTION, 
        reply_markup=get_language_keyboard()
    )
    
    # Set state to language selection
    await BotStates.language_selection.set()

async def process_language_selection(message: types.Message, state: FSMContext):
    """Process language selection"""
    user_id = message.from_user.id
    
    if message.text == "Русский":
        user_languages[user_id] = "ru"
        await message.answer(
            msgs_ru.MAIN_MENU,
            reply_markup=get_main_menu_keyboard("ru")
        )
    else:
        user_languages[user_id] = "kz"
        await message.answer(
            msgs_kz.MAIN_MENU,
            reply_markup=get_main_menu_keyboard("kz")
        )
    
    # Update state to main menu
    await BotStates.main_menu.set()

def register_handlers(dp: Dispatcher):
    """Register all common handlers"""
    dp.register_message_handler(cmd_start, commands=["start"], state="*")
    dp.register_message_handler(
        process_language_selection,
        lambda msg: msg.text in ["Русский", "Қазақша"],
        state=BotStates.language_selection
    )