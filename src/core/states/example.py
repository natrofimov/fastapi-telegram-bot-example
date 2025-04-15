from aiogram.fsm.state import StatesGroup, State


class ExampleStates(StatesGroup):
    waiting_for_message = State()
