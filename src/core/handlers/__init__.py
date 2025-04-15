from aiogram import Router

from .start import router as start_router
from .example import router as example_router

router = Router(name="main-router")

# here you need to include routers
router.include_routers(
    start_router,
    example_router,
)
