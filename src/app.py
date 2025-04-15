import asyncio

from aiogram import types
from fastapi import FastAPI, Request

from src import __version__
from src.lifespan import lifespan

app = FastAPI(
    title="FASTAPI Telegram Bot Template",
    lifespan=lifespan,
    version=__version__,
    description="# Description",
)


# controller for telegram updates
@app.post("/webhook", include_in_schema=False)
async def webhook(request: Request, update: dict) -> None:
    update = types.Update(**update)
    asyncio.create_task(request.app.state.dp.feed_update(request.app.state.bot, update))


@app.get("/")
async def root():
    return {
        "status": "Running",
        "version": __version__,
    }
