from aiogram import Router

from .answer import router as answer_router
from .common import router as common_router
from .extra import router as extra_router
from .prompt_menu import router as prompt_menu_router
from .start import router as start_router
from .statistics import router as statistics_router
from .short_request import router as short_request_router
from .text import router as text_router

router = Router(name="main-router")

router.include_routers(
    start_router,
    prompt_menu_router,
    common_router,
    extra_router,
    answer_router,
    statistics_router,
    short_request_router,
    text_router,
)
