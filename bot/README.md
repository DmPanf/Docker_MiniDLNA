## 


##  Что может делать этот Бот?
- 🕹 Управлять Сервисами
- ♻️ Перезапускать ПК
- 💾 Выводить статус данных
- 📡 Подключать VPN
- ⏳ Отключать Сервер


## Структура

<code>
.
├── data
│   └── config.py
├── filters
│   ├── __init__.py
│   └── is_reply.py
├── handlers
│   ├── general
│   │   ├── base.py
│   │   ├── errors.py
│   │   └── __init__.py
│   ├── groups
│   │   └── __init__.py
│   ├── __init__.py
│   └── private
│       └── __init__.py
├── __main__.py
├── middlewares
│   ├── __init__.py
│   └── throttling.py
├── misc
│   ├── bot_instance.py
│   ├── __init__.py
│   ├── keyboards
│   │   ├── __init__.py
│   │   └── source_markup.py
│   └── set_commands.py
├── __pycache__
│   └── __main__.cpython-310.pyc
└── stop.sh
</code>
