from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_faq_keyboard(lang):
    """FAQ inline keyboard based on language"""
    keyboard = InlineKeyboardMarkup(row_width=1)
    
    if lang == "ru":
        buttons = [
            InlineKeyboardButton("Как проводится отбор в программу?", callback_data="faq_how_to_apply"),
            InlineKeyboardButton("Что такое Izbasar?", callback_data="faq_what"),
            InlineKeyboardButton("Будет ли оплачиваться стажировка?", callback_data="faq_requirements"),
            InlineKeyboardButton("В какие регионы могут быть направлены финалисты?", callback_data="faq_final"),
        ]
    else:
        buttons = [
            InlineKeyboardButton("Бағдарламаға іріктеу қалай жүргізіледі?", callback_data="faq_how_to_apply"),
            InlineKeyboardButton("Izbasar деген не?", callback_data="faq_what"),
            InlineKeyboardButton("Тағылымдама ақылы бола ма?", callback_data="faq_requirements"),
            InlineKeyboardButton("Бағдарламаның финалистері қандай аймақтарға жіберілуі мүмкін?", callback_data="faq_final"),
        ]
    
    for button in buttons:
        keyboard.add(button)
        
    return keyboard