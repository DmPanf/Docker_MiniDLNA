## Список доступных Wi-Fi сетей

Для того чтобы узнать, какие Wi-Fi сети доступны, вы можете использовать команду `nmcli` или `iwlist`. Сначала убедитесь, что ваш Wi-Fi адаптер активирован. Вы можете использовать `nmcli` для просмотра списка всех сетевых интерфейсов:

```bash
nmcli device status
```

Если ваш Wi-Fi адаптер активен, вы должны увидеть его в списке, и он должен быть в состоянии `connected` или `disconnected`.

### Список доступных Wi-Fi сетей
Для просмотра списка доступных сетей используйте:

```bash
nmcli device wifi list
```

или

```bash
sudo iwlist [interface] scan
```

где `[interface]` — это имя вашего Wi-Fi адаптера (например, `wlan0`).

### Подключение к Wi-Fi сети
Для подключения к Wi-Fi сети вы можете использовать следующую команду:

```bash
nmcli device wifi connect [SSID] password [password]
```

где `[SSID]` — это имя сети, а `[password]` — пароль от неё.

### Настройка постоянного соединения
Чтобы ваше соединение стало постоянным, необходимо создать профиль NetworkManager для вашей сети. Обычно, если вы подключаетесь через `nmcli` или графический интерфейс NetworkManager, такой профиль создается автоматически. Вы можете проверить существующие профили, используя:

```bash
nmcli connection show
```

Если нужный профиль уже существует, он будет автоматически использован для подключения при каждой загрузке системы, при условии, что NetworkManager настроен на автозапуск.

Если вы хотите настроить все вручную, вы можете создать конфигурационный файл в `/etc/NetworkManager/system-connections/` (но это обычно не требуется для большинства пользователей).

---

## пример Bash-скрипта для интерактивной настройки интерфейса Wi-Fi и подключения к выбранной пользователем сети:

1. Сохраните код в файл, например, `setup_wifi.sh`.
2. Сделайте файл исполняемым: `chmod +x setup_wifi.sh`.
3. Запустите скрипт с правами администратора: `sudo ./setup_wifi.sh`.

```bash
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
```

**Примечание:** Этот скрипт предполагает, что у вас уже установлен и настроен NetworkManager, и ваш Wi-Fi адаптер уже инициализирован и готов к использованию. Skрипт также не проверяет наличие ошибок на каждом этапе; он представляет собой базовый пример.

---
## инструкция для Ubuntu:

<code>
sudo apt update
sudo apt dist-upgrade
sudo apt-get install linux-headers-generic build-essential dkms git
git clone "https://github.com/RinCat/RTL88x2BU-Linux-Driver.git" /usr/src/rtl88x2bu-git
sudo sed -i 's/PACKAGE_VERSION="@PKGVER@"/PACKAGE_VERSION="git"/g' /usr/src/rtl88x2bu-git/dkms.conf
sudo dkms add -m rtl88x2bu -v git
sudo dkms autoinstall
sudo reboot now
sudo modprobe 88x2bu
</code>


## Для установки драйвера на Manjaro Linux, вы можете воспользоваться инструкцией для Ubuntu с небольшими изменениями. Вот как это сделать:

1. Обновите свою систему:
    ```
    sudo pacman -Syu
    ```

2. Установите необходимые зависимости:
    ```
    sudo pacman -S linux-headers base-devel dkms git
    ```
    Если у вас установлено несколько версий ядра, удостоверьтесь, что вы установили заголовки для той версии, которую используете. Например, для ядра `linux54`, команда будет выглядеть так:
    ```
    sudo pacman -S linux54-headers
    ```

3. Клонируйте репозиторий:
    ```
    git clone "https://github.com/RinCat/RTL88x2BU-Linux-Driver.git" /usr/src/rtl88x2bu-git
    ```

4. Измените файл `dkms.conf` в клонированной папке:
    ```
    sudo sed -i 's/PACKAGE_VERSION="@PKGVER@"/PACKAGE_VERSION="git"/g' /usr/src/rtl88x2bu-git/dkms.conf
    ```

5. Добавьте модуль к DKMS:
    ```
    sudo dkms add -m rtl88x2bu -v git
    ```

6. Произведите автоматическую установку модуля:
    ```
    sudo dkms autoinstall
    ```

7. Перезагрузите компьютер:
    ```
    sudo reboot now
    ```

8. Загрузите модуль:
    ```
    sudo modprobe 88x2bu
    ```

После этих шагов ваш адаптер должен заработать. Если у вас возникнут проблемы, убедитесь, что вы правильно выполнили все шаги.

```bash
sudo git clone "https://github.com/RinCat/RTL88x2BU-Linux-Driver.git" /usr/src/rtl88x2bu-git
```

Это даст вам необходимые права для клонирования репозитория в эту директорию. Если же вы не хотите использовать `sudo` для этого, вы можете клонировать репозиторий в вашу домашнюю директорию, а затем переместить его в `/usr/src` с использованием `sudo`:

```bash
git clone "https://github.com/RinCat/RTL88x2BU-Linux-Driver.git"
sudo mv RTL88x2BU-Linux-Driver /usr/src/rtl88x2bu-git
```

Таким образом, вы сначала клонируете репозиторий в директорию, где у вас есть права доступа, а затем перемещаете его в `/usr/src`, используя `sudo`.

## пример интерактивного скрипта на Bash для первичной установки драйвера `rtl88x2bu` на Manjaro Linux

Для того чтобы использовать этот скрипт:

1. Сохраните код в файл, например, `install_rtl88x2bu.sh`.
2. Сделайте файл исполняемым: `chmod +x install_rtl88x2bu.sh`.
3. Запустите скрипт с правами администратора: `sudo ./install_rtl88x2bu.sh`.

```bash
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
```

**Примечание:** Этот скрипт не проверяет наличие ошибок на каждом этапе, так что в случае возникновения проблем его выполнение может быть прервано. Это лишь базовый пример, и вы можете дополнить его дополнительными проверками и функциями по вашему усмотрению.
