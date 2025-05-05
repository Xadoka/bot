# utils/states.py
from aiogram.dispatcher.filters.state import State, StatesGroup

class BotStates(StatesGroup):
    """States for the Izbasar bot"""
    language_selection = State()  # User is selecting language
    main_menu = State()          # User is in main menu
    candidate_menu = State()     # User is in candidate menu

