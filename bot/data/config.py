from envparse import env

# Simply reads env file and assigns token variable
env.read_envfile()
#BOT_TOKEN = env.str("BOT_TOKEN")
BOT_TOKEN = env.str("TOKEN_31")
myID = env.str("USER_ID1")
#ID0 = env.str(ID[0])

# Whether to skip updates or not
skip_updates = False

# List of commands
commands = (
    ('help', 'Вывести справку 💡'),
    ('mems', 'Шпаргалка 🗄'),
    ('weather', 'Прогноз погоды 24ч 🌤'),
    ('dlna_on', 'Перезапустить DLNA 📺'),
    ('dlna_off', 'Запретить DLNA 🔞'),
    ('vpn_on', 'Включение VPN 📡'),
    ('vpn_off', 'Включение VPN 🚳'),
    ('admin_on', 'Разрешить соединение по SSH 🌐'),
    ('admin_off', 'Запретить соединение по SSH 🚷'),
    ('anydesk_on', 'Разрешить доступ к экрану 🈴'),
    ('anydesk_off', 'Запретить доступ к экрану 📵'),
    ('bot_on', 'Запустить Бот Admin_Linux ⚙️'),
    ('bot_off', 'Остановить Бот Admin_Linux 🚭'),
    ('stop', 'Закончить работу бота 🚱'),
    ('restart', 'Перезапуск Сервера кино ♻️'),
    ('shutdown', 'Отключение Сервера! 🔴'),
)
