#!/bin/bash

# Проверка прав администратора
if [[ $EUID -ne 0 ]]; then
   echo "Этот скрипт должен быть запущен с правами администратора."
   exit 1
fi

# Просмотр сетевых интерфейсов
echo "Просмотр сетевых интерфейсов..."
nmcli device status

# Вывод списка доступных Wi-Fi сетей
echo "Поиск доступных Wi-Fi сетей..."
nmcli device wifi list

# Выбор сети для подключения
read -p "Введите SSID сети для подключения: " SSID

# Ввод пароля
read -sp "Введите пароль от сети (если есть): " PASSWORD
echo ""

# Подключение к сети
if [ -z "$PASSWORD" ]; then
    echo "Подключение к открытой сети..."
    nmcli device wifi connect "$SSID"
else
    echo "Подключение к защищенной сети..."
    nmcli device wifi connect "$SSID" password "$PASSWORD"
fi

# Проверка статуса подключения
if [ $? -eq 0 ]; then
    echo "Успешно подключено к $SSID."
else
    echo "Не удалось подключиться к $SSID. Пожалуйста, проверьте ваш SSID и пароль, и попробуйте снова."
fi
