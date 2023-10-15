import hashlib

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

HASHED_PASSWORD = "your_hashed_password_here"  # Сохраните хэш вашего пароля здесь

class AuthMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        hashed_input = hashlib.sha256(message.text.encode()).hexdigest()
        
        if hashed_input == HASHED_PASSWORD:
            data['is_authenticated'] = True
        else:
            data['is_authenticated'] = False

    async def on_post_process_message(self, message: types.Message, result: dict, data: dict):
        is_authenticated = data.get('is_authenticated', False)
        
        if not is_authenticated:
            await message.answer("Incorrect password. Try again.")
