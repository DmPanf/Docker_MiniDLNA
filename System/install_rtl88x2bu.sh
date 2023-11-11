#!/bin/bash

# Проверка прав администратора
if [[ $EUID -ne 0 ]]; then
   echo "Этот скрипт должен быть запущен с правами администратора"
   exit 1
fi

# Обновление системы
echo "Обновление системы..."
sudo pacman -Syu --noconfirm

# Установка зависимостей
echo "Установка зависимостей..."
sudo pacman -S --noconfirm linux-headers base-devel dkms git

# Клонирование репозитория драйвера
echo "Клонирование репозитория драйвера..."
sudo git clone "https://github.com/RinCat/RTL88x2BU-Linux-Driver.git" /usr/src/rtl88x2bu-git

# Изменение файла dkms.conf
echo "Изменение файла dkms.conf..."
sudo sed -i 's/PACKAGE_VERSION="@PKGVER@"/PACKAGE_VERSION="git"/g' /usr/src/rtl88x2bu-git/dkms.conf

# Добавление модуля в DKMS
echo "Добавление модуля в DKMS..."
sudo dkms add -m rtl88x2bu -v git

# Автоматическая установка модуля
echo "Автоматическая установка модуля..."
sudo dkms autoinstall

# Перезагрузка
read -p "Перезагрузить сейчас? (y/n): " choice
if [[ $choice == 'y' || $choice == 'Y' ]]; then
    echo "Перезагрузка..."
    sudo reboot now
else
    echo "Перезагрузите систему вручную, чтобы завершить установку."
fi
