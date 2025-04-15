import pathlib

from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.config import settings
from src.core.keyboards.reply import admins_only_keyboard, test_keyboard
from src.utils import logger

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent.parent
router = Router(name="start-router")


@router.message(CommandStart())
async def command_start_handler(
    message: Message,
    state: FSMContext,
    # need to use some Bot method? Just add it like this in handler args!
    bot: Bot,
) -> None:
    await state.clear()

    # is admin check
    is_admin = message.from_user.id in settings.admins.ids
    keyboard = admins_only_keyboard if is_admin else test_keyboard
    text = (
        f"✅ Admin: {message.from_user.full_name}"
        if is_admin
        else f"❌ Not admin: {message.from_user.full_name}"
    )

    await message.answer(text, reply_markup=keyboard)

    # you can now use aiogram.Bot methods without importing it directly into module
    result = await bot.me()
    logger.debug("getMe result: %s", result)
