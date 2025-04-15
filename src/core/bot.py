from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.chat_action import ChatActionMiddleware

from src.config import settings
from src.core.handlers import router as main_router
from src.utils import logger


class BotApplication:
    def __init__(self) -> None:
        self.dp = Dispatcher()
        self.bot = Bot(
            token=settings.tokens.telegram,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )

    async def on_webhook(self) -> None:
        await self.__include_handlers()
        await self.__register_middlewares()
        await self.__set_commands()
        await self.__set_description()
        await self.__set_webhook()

    async def start_polling(self) -> None:
        await self.__include_handlers()
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.__register_middlewares()
        await self.__set_commands()
        await self.__set_description()
        await self.dp.start_polling(
            self.bot,
        )

    async def on_shutdown(self) -> None:
        await self.bot.delete_webhook()
        await self.bot.session.close()

    # use this to include update handlers
    async def __include_handlers(self) -> None:
        self.dp.include_router(main_router)

    async def __register_middlewares(self) -> None:
        self.dp.message.middleware(ChatActionMiddleware())

    async def __set_webhook(self) -> None:
        await self.bot.set_webhook(
            url=f"https://{settings.host.address}/webhook",
        )
        logger.info("Webhook info: %s", await self.bot.get_webhook_info())

    # use this to set up commands
    async def __set_commands(self) -> None:
        await self.bot.set_my_commands(
            [
                types.BotCommand(
                    command="start",
                    description="🚀 Начать взаимодействие",
                ),
            ]
        )

    # use this to set up LONG description
    async def __set_description(self) -> None:
        await self.bot.set_my_description(description="🔥 TEST DESCRIPTION")
