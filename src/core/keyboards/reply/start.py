import copy

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

test_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🔥 Example button 1"),
        ],
        [
            KeyboardButton(text="🔥 Example button 2"),
        ],
    ],
)

admins_only_keyboard = copy.deepcopy(test_keyboard)
admins_only_keyboard.keyboard[-1].append(
    KeyboardButton(text="✨ Button for admins only"),
)