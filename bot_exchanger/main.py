import os
import json
import logging
import asyncio

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.message import ParseMode

from bot.config import TELEGRAM_TOKEN
from bot.handlers import register_handlers
from bot.filters import bind_filters

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

storage = MemoryStorage()

bot = Bot(TELEGRAM_TOKEN, loop=loop, validate_token=True)
dp = Dispatcher(bot, storage=storage)


async def on_startup(dispatcher: Dispatcher):
    await bind_filters(dispatcher)
    await register_handlers(dispatcher)


executor.start_polling(dp, loop=loop, on_startup=on_startup)