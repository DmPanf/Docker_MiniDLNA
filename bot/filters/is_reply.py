from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class IsReply(BoundFilter):
    """Checks if message is reply to another message"""

    async def check(self, message: types.Message):
        myMsg = 'ID: <b>' + str(message.chat.id) + '</b>'
#        await message.answer(myMsg, parse_mode=ParseMode.MARKDOWN)
#        await bot.send_message(ID[0], myMsg, parse_mode=ParseMode.MARKDOWN) # Main Admin
#        return message.reply_to_message
        return message.answer(myMsg)
