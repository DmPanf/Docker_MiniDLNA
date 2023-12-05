## Services

Для хранения пароля в безопасной форме, можно использовать хэш-функцию, такую как SHA-256.

### Вариант `middlewares/auth_middleware.py`

```python
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
```

### Консольная программа для генерации хэша

Простая консольная программа для генерации хэша пароля. Этот хэш затем можно сохранить в файле `auth_middleware.py`.

```python
import hashlib

def generate_hash():
    password = input("Enter the password you want to hash: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(f"The hashed password is: {hashed_password}")

if __name__ == "__main__":
    generate_hash()
```

- Выполнив эту программу, надо ввести пароль, который будет использован для аутентификации, и программа выдаст хэш. 
- Далее надо скопировать этот хэш и сохранить его в переменной `HASHED_PASSWORD` в файле `auth_middleware.py`.
- Таким образом, вы можно хранить пароль в безопасной форме и использовать его для аутентификации.

---

###

