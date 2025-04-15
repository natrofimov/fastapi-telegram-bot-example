import pathlib

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message

from src.config import settings
from src.core.integrations import Graspil
from src.core.keyboards.inline.menu_inline_keyboards import show_template_keyboard
from src.core.keyboards.reply.menu_keyboards import admin_keyboard, main_keyboard
from src.core.repositories import GreetingsRepository, UsersRepository
from src.core.schemas.db import UserSchemaAdd

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent.parent
router = Router(name="start-router")


@router.message(CommandStart())
async def command_start_handler(
    message: Message,
    state: FSMContext,
) -> None:
    await state.clear()
    # send stats
    graspil = Graspil()
    await graspil.write_action(target_id=10459, telegram_id=message.from_user.id)

    is_admin = message.from_user.id in settings.admins.ids
    keyboard = admin_keyboard if is_admin else main_keyboard

    greetings_repository = GreetingsRepository()
    users_repository = UsersRepository()

    exists = bool(
        await users_repository.get_by_filter(telegram_id=message.from_user.id)
    )
    if not exists:
        schema = UserSchemaAdd(
            telegram_id=message.from_user.id,
            name=message.from_user.full_name,
            username=message.from_user.username,
            language_code=message.from_user.language_code,
        ).model_dump()
        await users_repository.add(schema)

        greeting = await greetings_repository.get_by_filter(type="first-time")
        # sending greeting for new user
        file = FSInputFile(
            path=BASE_DIR / "files" / "videos" / greeting.filename,
            filename="greeting.mp4",
        )

        await message.answer(
            text=str(greeting.text),
            reply_markup=keyboard,
        )
        await message.answer_video(file, reply_markup=show_template_keyboard)

    else:
        greeting = await greetings_repository.get_by_filter(type="common")

        # Mapped[str] to str
        greeting_text: str = str(greeting.text)

        await message.answer(
            greeting_text,
            reply_markup=keyboard,
        )
        await message.answer(
            f"👇 Нажмите на кнопку, чтобы увидеть пример хорошего запроса",
            reply_markup=show_template_keyboard,
        )
