import os

from aiogram import types
from misc import dp, bot
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, hbold, bold, italic, code, pre, link, escape_md
from . import keyboards  
from . import sqlite

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.db")
db = sqlite.SQLite(db_path)
	

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	if not db.subscriber_exists(message.from_user.id):
		db.add_subscriber(message.from_user.id)
	db.save()
	message_text = 'Привет!\nНапиши /help, чтобы получить список возможных команд.'
	await bot.send_message(message.from_user.id, message_text)

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
	await bot.send_message(message.from_user.id,
							'/start - начать общение с ботом\n' + 
							'/help - вывести список команд\n' + 
							'/sign_up - оформить заявку на запись\n' + 
							'/price_list - получить перечень предоставляемых услуг и их стоимость\n'+ 
							'/working_hours - получить график работы\n' +
							'/contacts - получить контактную информацию\n' +
							'/exit - завершить общение')

@dp.message_handler(commands=['sign_up'])
async def process_command_1(message: types.Message):
	db.update_subscription(message.from_user.id, True)
	db.save()
	message_text = 'Отлично, сейчас примем заявку на запись.\n\nПришлите ваш номер телефона(начиная с 7) и наш специалист свяжется с вам в течение 10 минут.'
	await bot.send_message(message.from_user.id, message_text)

@dp.message_handler(commands=['price_list'])
async def inf_return(message: types.Message):
	message_text = text(bold('Предоставляемые услуги:\n') +
			'Стрижка классическая мужская - ' + bold('100 рублей\n') +
			'Стридка классическая женская - ' + bold('200 рублей\n') +
			'Покраска волос - ' + bold('100 рублей\n') +
			'Все остальное - дорого рублей')
	await bot.send_message(message.from_user.id, message text)
	await bot.send_message(message.from_user.id, 'Желаете записаться?', reply_markup=keyboards.sign_up_kb, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['working_hours'])
async def inf_return(message: types.Message):
	message_text = text('Наш центр работает на ' + 
						'ул. Пушкина, д. 15\n' + 
						'ПН - ВС\n' + 
						'9:00 - 20:00')
	await bot.send_message(message.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN)
	await bot.send_message(message.from_user.id, 'Желаете записаться?', reply_markup=keyboards.sign_up_kb, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['contacts'])
async def inf_return(message: types.Message):
	message_text = text(bold('Телефоны:\n') + 
						italic('80950591731\n80721278538\n') +
						bold('Сайт:\n') + 
						'blabla.com\n' + 
						bold('Mail:\n') + 
						'bla@bla.com')
	await bot.send_message(message.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN)
	await bot.send_message(message.from_user.id, 'Желаете записаться?', reply_markup=keyboards.sign_up_kb, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['path'])
async def path_return(message: types.Message):
	await bot.send_message(message.from_user.id, BASE_DIR)	
	
@dp.message_handler(commands=['exit'])
async def inf_return(message: types.Message):
	message_text = 'Буду ждать вашего возвращения. Если захотите возобновить диалог, просто напишите /start.'
	await bot.send_message(message.from_user.id, message_text)
