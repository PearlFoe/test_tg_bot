from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

sign_up_btn_1 = InlineKeyboardButton('Хочу записаться', callback_data = 'sign_up_agreement')
sign_up_btn_2 = InlineKeyboardButton('Не хочу записыватсья', callback_data = 'sign_up_disagreement')

sign_up_kb = InlineKeyboardMarkup()
sign_up_kb.add(sign_up_btn_1) 
sign_up_kb.add(sign_up_btn_2)