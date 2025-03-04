import ast
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from Data import Data
from WhisperBot.database.whisper_sql import Whispers
from WhisperBot.database import SESSION
from WhisperBot.bot_users import check_for_users


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot, callback_query: CallbackQuery):
	user = await bot.get_me()
	mention = user["mention"]
	if callback_query.data.lower() == "home":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.START.format(callback_query.from_user.mention, mention),
			reply_markup=InlineKeyboardMarkup(Data.buttons),
		)
	elif callback_query.data.lower() == "about":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.ABOUT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons),
		)
	elif callback_query.data.lower() == "help":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text="**Veja como me usar**\n" + Data.HELP,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons),
		)
	else:
		cb_data = callback_query.data
		data_list = ast.literal_eval(str(cb_data))
		if callback_query.from_user.id in data_list:
			specific = callback_query.inline_message_id
			q = SESSION.query(Whispers).get(specific)
			if q:
				await callback_query.answer(q.message, show_alert=True)
			else:
				await callback_query.answer("Message Not Found", show_alert=True)
			SESSION.commit()
		else:
			await callback_query.answer("Desculpe baianor, você não pode ver esta mensagem privada, porque isso não é para você... No caso, você perderia seu tempo vindo aqui? Deixe de curiosidade e vai lavar uma louça 🤡!", show_alert=True)
		await check_for_users(data_list)
