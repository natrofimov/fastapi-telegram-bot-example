from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from src.core.callback_data import ExampleCallbackData
from src.core.keyboards.inline import example_inline_keyboard
from src.core.states import ExampleStates

router = Router(name="example-router")


# handle reply keyboard button clicks
@router.message(F.text == "🔥 Example button 1")
async def button_1_handler(message: Message) -> None:
    await message.answer(
        f"✔ Example button 1 clicked!\nYour data:\n"
        f"1. Name: <strong>{message.from_user.first_name}</strong>\n"
        f"2. Second name: <strong>{message.from_user.last_name}</strong>\n"
        f"3. Telegram ID: <strong>{message.from_user.id}</strong>\n"
        f"4. Premium: <strong>{message.from_user.is_premium}</strong>\n"
    )


@router.message(F.text == "✳ Button for admins only")
async def button_1_handler(message: Message, bot: Bot) -> None:
    await message.answer(
        f"✅ Success!\n\n🥇 You are an admin of this bot:\n"
        f"<pre>{await bot.me()}</pre>"
    )


@router.message(F.text == "⌨ Show inline keyboard")
async def show_inline_keyboard_handler(message: Message) -> None:
    await message.answer(
        "Example of inline keyboard", reply_markup=example_inline_keyboard
    )


# handle inline keyboard clicks and process data
@router.callback_query(ExampleCallbackData.filter())
async def example_callback_query_handler(
    callback: CallbackQuery,
    # that's how you can access data you put into button
    callback_data: ExampleCallbackData,
) -> None:
    value = callback_data.value
    description = callback_data.description

    # stop the "loading" animation on the user's button, send answer
    await callback.answer("Success")

    await callback.message.answer(
        f"✅ Button pressed!\n"
        f"CALLBACK DATA:\n"
        f"VALUE: {value}\n"
        f"DESCRIPTION: {description}\n"
    )


# handle states
@router.message(F.text == "⚙️ Change state")
async def change_state_handler(
    message: Message,
    # that's how you can use state in your handlers
    state: FSMContext,
) -> None:
    await state.set_state(ExampleStates.waiting_for_message)

    # that's how you can save data in states (data will not be cleared if you change state)
    await state.set_data(data={"example_data": "example"})

    await message.answer(
        "✅ <strong>State changed! Data saved! Type anything to test it!</strong>\n\nTo <strong>reset</strong> it, type /start"
    )


@router.message(ExampleStates.waiting_for_message)
async def any_message_handler(
    message: Message,
    state: FSMContext,
) -> None:
    await message.answer(
        f"⭐ Current state: {await state.get_state()}\n\n📦 STATE DATA: {await state.get_data()}"
    )
    await state.clear()
