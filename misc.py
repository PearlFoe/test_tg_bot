import logging
import config
from aiogram import Bot, Dispatcher

bot = Bot(token=config.token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)