import os
import config
import aiohttp
import handlers

from aiogram import Bot, types
from misc import dp
from aiogram.utils import executor
from aiogram.dispatcher.webhook import get_new_configured_app

PROJECT_NAME = 'warm-reaches-60292'

WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com'
WEBHOOK_URL_PATH = f'/webhook/{config.token}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_URL_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT')

async def on_startup(app):
	await bot.delete_webhook()
	await bot.set_webhook(WEBHOOK_URL)

if __name__ == '__main__':
	if "HEROKU" in list(os.environ.keys()):
		app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
		app.on_startup.append(on_startup)
		dp.loop.set_task_factory(context.task_factory)
		web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)  # Heroku stores port you have to listen in your app
	else:
		executor.start_polling(dp)

#https://github.com/gurland/aiogram_heroku/blob/master/bot.py




