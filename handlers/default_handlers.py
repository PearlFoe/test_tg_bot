import os

from aiogram import types
from misc import dp, bot
from . import sqlite

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.db")
db = sqlite.SQLite(db_path)

@dp.callback_query_handler(lambda c: c.data == 'sign_up_agreement')
async def sing_up_process(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	db.update_subscription(callback_query.from_user.id, True)
	db.save()
	message_text = 'Отлично, сейчас примем заявку на запись.\n\nПришлите ваш номер телефона(начиная с 7) и наш специалист свяжется с вам в течение 10 минут.'
	await bot.send_message(callback_query.from_user.id, message_text)

@dp.callback_query_handler(lambda c: c.data == 'sign_up_disagreement')
async def sign_up_disagreement(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	message_text = 'Хорошо, для полуячения дополнительной информации напишите /help.'
	await bot.send_message(callback_query.from_user.id, message_text)

@dp.message_handler(lambda c: c.text.isnumeric() == True and db.check_sign_up_status(c.from_user.id) == True)
async def getting_telephone_number(message: types.Message):
	if len(message.text) == 11:
		message_text = ('Ваша заявка была принята. Ожидайте звонка специалиста. В течение 10 минут с вами свяжутся для подтверждения записи.\n\n'+
							'Если вы не верно указали свои контактные данны, введите команду /sign_up и пройдите процедуру записи еще раз.\n\n'+
							'Для получения дополнительной информации введите команду /help.')
		await bot.send_message(message.from_user.id, message_text)
		db.add_telephone_number(message.from_user.id, message.text)
		db.update_subscription(message.from_user.id, False)
		db.save()
	else:
		message_text = 'Что-то пошло не так. Пришлите нам еще раз свой номер телефона начиная с 7.'
		await bot.send_message(message.from_user.id, message_text)






#ловим мусор
@dp.message_handler(content_types=types.ContentType.ANY)
async def unknown_message(message: types.Message):
    message_text = 'Упс, я не знаю, что с этим делать. Напиши /help для получения списка команд.'
    await bot.send_message(message.from_user.id, message_text)
