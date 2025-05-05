# handlers/candidate.py
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from config.bot_config import bot
from utils.states import BotStates
from keyboards.reply_keyboards import get_main_menu_keyboard, get_candidate_menu_keyboard
from keyboards.inline_keyboards import get_faq_keyboard
import content.messages_ru as msgs_ru
import content.messages_kz as msgs_kz
from config.constants import RESOURCES

# Import user language dictionary
from handlers.common import user_languages

async def enter_candidate_menu(message: types.Message, state: FSMContext):
    """Handle entering candidate menu"""
    user_id = message.from_user.id
    lang = user_languages.get(user_id, "ru")
    
    # Show candidate menu
    msgs = msgs_ru if lang == "ru" else msgs_kz
    await message.answer(
        msgs.MAIN_MENU,
        reply_markup=get_candidate_menu_keyboard(lang)
    )
    
    # Update state
    await BotStates.candidate_menu.set()

async def back_to_main_menu(message: types.Message, state: FSMContext):
    """Handle going back to main menu"""
    user_id = message.from_user.id
    lang = user_languages.get(user_id, "ru")
    
    msgs = msgs_ru if lang == "ru" else msgs_kz
    await message.answer(
        msgs.BACK_TO_MENU,
        reply_markup=get_main_menu_keyboard(lang)
    )
    
    # Update state
    await BotStates.main_menu.set()

async def show_program_info(message: types.Message):
    """Show program information"""
    user_id = message.from_user.id
    lang = user_languages.get(user_id, "ru")
    
    msgs = msgs_ru if lang == "ru" else msgs_kz
    await message.answer(
        msgs.PROGRAM_INFO,
        parse_mode="Markdown"
    )

async def show_application_rules(message: types.Message):
    """Show application rules"""
    user_id = message.from_user.id  
    lang = user_languages.get(user_id, "ru")
    
    msgs = msgs_ru if lang == "ru" else msgs_kz
    await message.answer(
        msgs.APPLICATION_RULES,
        parse_mode="Markdown"
    )

async def show_faq(message: types.Message):
    """Show FAQ inline keyboard"""
    user_id = message.from_user.id
    lang = user_languages.get(user_id, "ru")
    
    msgs = msgs_ru if lang == "ru" else msgs_kz
    await message.answer(
        msgs.FAQ_SELECTION,
        reply_markup=get_faq_keyboard(lang)
    )

async def show_contacts(message: types.Message):
    """Show contact information"""
    user_id = message.from_user.id
    lang = user_languages.get(user_id, "ru")
    
    msgs = msgs_ru if lang == "ru" else msgs_kz
    await message.answer(
        msgs.CONTACT_INFO,
        parse_mode="Markdown"
    )

def register_handlers(dp: Dispatcher):
    """Register candidate handlers"""
    # Main menu selection
    dp.register_message_handler(
        enter_candidate_menu,
        lambda msg: msg.text in ["📝 Я кандидат", "📝 Мен кандидатпын"],
        state=BotStates.main_menu
    )
    
    # Back button
    dp.register_message_handler(
        back_to_main_menu,
        lambda msg: msg.text in ["🔙 Назад", "🔙 Артқа"],
        state=BotStates.candidate_menu
    )
    
    # Candidate menu options
    dp.register_message_handler(
        show_program_info,
        lambda msg: msg.text in ["ℹ Информация о программе", "ℹ Бағдарлама жайлы ақпарат"],
        state=BotStates.candidate_menu
    )
    
    dp.register_message_handler(
        show_application_rules,
        lambda msg: msg.text in ["📄 Правила подачи заявок", "📄 Өтінім беру ережелері"],
        state=BotStates.candidate_menu
    )
    
    dp.register_message_handler(
        show_faq,
        lambda msg: msg.text in ["❔ Часто задаваемые", "❔ Жиі қойылатын сұрақтар"],
        state=BotStates.candidate_menu
    )
    
    dp.register_message_handler(
        show_contacts,
        lambda msg: msg.text in ["📞 Контакты", "📞 Бізбен байланысу"],
        state=BotStates.candidate_menu
    )

    