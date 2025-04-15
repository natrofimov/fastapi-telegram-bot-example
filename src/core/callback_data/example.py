from aiogram.filters.callback_data import CallbackData


class ExampleCallbackData(CallbackData, prefix="example"):
    value: str
    description: str
