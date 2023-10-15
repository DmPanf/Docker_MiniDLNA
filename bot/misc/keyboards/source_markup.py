from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Creating an inline keyboard
source_markup = InlineKeyboardMarkup()

# Inserting the source code button with a specific url
#source_markup.insert(InlineKeyboardButton('My Sources!', url='https://gitlab.com/comictomcat/aiogram-template'))
source_markup.insert(InlineKeyboardButton('💡 Documentation', url='https://docs.docker.com/engine/reference/commandline/pull/'))
source_markup.insert(InlineKeyboardButton('💠 81 Command', url='https://www.fosstechnix.com/docker-command-cheat-sheet/'))
source_markup.insert(InlineKeyboardButton('🔐 WireGuard', url='https://noostyche.ru/blog/2022/03/29/ispolzovanie-wireguard-klientami-s-serymi-ip/'))
