from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_language_keyboard():
    """Keyboard for language selection"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton("Русский"),
        KeyboardButton("Қазақша")
    )
    return keyboard

def get_main_menu_keyboard(lang):
    """Main menu keyboard based on language"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    if lang == "ru":
        keyboard.add(KeyboardButton("📝 Я кандидат"))
    else:
        keyboard.add(KeyboardButton("📝 Мен кандидатпын"))
            
    return keyboard

def get_candidate_menu_keyboard(lang):
    """Candidate menu keyboard based on language"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    if lang == "ru":
        keyboard.add(KeyboardButton("ℹ Информация о программе"))
        keyboard.add(KeyboardButton("📄 Правила подачи заявок"))
        keyboard.add(KeyboardButton("❔ Часто задаваемые"))
        keyboard.add(KeyboardButton("📞 Контакты"))
        keyboard.add(KeyboardButton("🔙 Назад"))
    else:
        keyboard.add(KeyboardButton("ℹ Бағдарлама жайлы ақпарат"))
        keyboard.add(KeyboardButton("📄 Өтінім беру ережелері"))
        keyboard.add(KeyboardButton("❔ Жиі қойылатын сұрақтар"))
        keyboard.add(KeyboardButton("📞 Бізбен байланысу"))
        keyboard.add(KeyboardButton("🔙 Артқа"))
        
    return keyboard