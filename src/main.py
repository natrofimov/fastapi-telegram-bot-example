# use this script to run bot locally
import asyncio

if __name__ == "__main__":
    from src.core.bot import BotApplication

    bot_app = BotApplication()
    asyncio.run(bot_app.start_polling())
