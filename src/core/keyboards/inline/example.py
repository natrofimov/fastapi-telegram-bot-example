from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.core.callback_data import ExampleCallbackData

# you can pass any data into inline keyboard buttons
example_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Example button 1",
                callback_data=ExampleCallbackData(
                    value="Some value 1",
                    description="Some description 1",
                ).pack(),
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ Example button 2",
                callback_data=ExampleCallbackData(
                    value="Some value 2",
                    description="Some description 2",
                ).pack(),
            ),
        ],
    ]
)
