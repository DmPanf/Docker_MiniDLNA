from aiogram import types
from aiogram.utils.markdown import hcode

from bot.misc import dp
import bot.data.config as config

from bot.middlewares import rate_limit
from bot.misc.keyboards import source_markup
import subprocess # Для запуска скриптов и команд Linux


@dp.message_handler(commands="start")
async def start(message: types.Message):
    """Responds to /start with greeting and inline keyboard,
    which's located in misc/keyboards/source_markup.py"""
    await message.answer(f"Hello there, {message.from_user.full_name}!",
                         reply_markup=source_markup)


@dp.message_handler(commands="dlna_off")
async def dlna_off(message: types.Message):
#    if PASS and str(message.chat.id) in str(ID):
#       await message.answer('*⏱  ждем загрузку ПК ...*', parse_mode=ParseMode.MARKDOWN)
#       await message.answer('*⏱  ждем загрузку ПК ...*', parse_mode=ParseMode.MARKDOWN, show_alert=True) # Ошибка ALERT нут здесь = inline
#       await message.answer('<b>⏱  ждем отключение сервиса ...</b>', parse_mode=ParseMode.HTML)
#       subprocess.call(['/bin/bash', myDir + '/scripts/shutdown.sh', 'r'])
       subprocess.call(['/bin/bash', 'stop.sh'])
#       subprocess.call(['/usr/bin/sudo', '/usr/sbin/init', '6'])
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
#    else:
#       return True


@rate_limit(5, "help")
@dp.message_handler(commands="help")
async def commands(message: types.Message):
    """Responds to /help with list of available commands,
    which're located in data/config.py"""

    # Generates a list
    answer = ["Available commands: "]
    for command, description in config.commands:
        answer.append(hcode(f"/{command}") + f" — {description}")

    await message.answer("\n".join(answer))
