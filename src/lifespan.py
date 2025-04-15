from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.bot import BotApplication


@asynccontextmanager
async def lifespan(app: FastAPI):
    bot_app = BotApplication()

    # add dependencies to state
    app.state.dp = bot_app.dp
    app.state.bot = bot_app.bot

    await bot_app.on_webhook()

    yield

    await bot_app.on_shutdown()
