# README.md for check_ssh_tunnel.sh

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This script (`check_ssh_tunnel.sh`) is designed to automatically manage an SSH tunnel and a FastAPI container. The script checks the status of both the SSH tunnel and the FastAPI container running in Docker. Depending on their statuses, it takes appropriate actions to either establish or terminate the SSH tunnel.

## Installation

### Prerequisites

The script has the following dependencies:

- SSH client
- Docker
- `ps`, `grep`, and `pkill` command-line utilities

Please make sure these dependencies are installed on your system.

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/dmpanf/your-repository-name.git
    ```

2. Navigate to the directory:

    ```bash
    cd your-repository-name
    ```

3. Make the script executable:

    ```bash
    chmod +x check_ssh_tunnel.sh
    ```

4. Copy or create the `config.sh` file in the same directory as `check_ssh_tunnel.sh`. Example `config.sh` content:

    ```bash
    SSH_PORT=53217
    SSH_KEY="id_ed25519.vps1-ru"
    ```

5. Update the `.gitignore` file to ignore the `config.sh`:

    ```bash
    echo "config.sh" >> .gitignore
    ```

## Usage

To run the script, execute:

```bash
./check_ssh_tunnel.sh
```

To set up a crontab to run this script every 3 minutes, execute:

```bash
(crontab -l ; echo "*/3 * * * * /path/to/check_ssh_tunnel.sh") | crontab -
```

## Customization

All customization can be done via the `config.sh` file or directly in the `check_ssh_tunnel.sh` script. You can set the following:

- Docker container name (`DOCKER_NAME`)
- Remote and Local port numbers (`REMOTE_PORT` and `LOCAL_PORT`)
- Remote User and Server (`REMOTE_USER_SERVER`)
- SSH Port (`SSH_PORT`)
- SSH Key (`SSH_KEY`)

## Contributing

Contributions, issues, and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Author: Dmitrii 
- GitHub: [dmpanf](https://github.com/dmpanf)

---

Feel free to use this README as a template for your GitHub repository. Modify it according to your project's needs.
---


## ASCII

ASCII-схемы обычно очень просты, но они могут быть полезны для визуализации базовых концепций. Вот пример схемы, которая может иллюстрировать взаимодействие между двумя серверами:

```
                     +-------------+
                     |   Client    |  
                     | (FastAPI)   |
                     +------+------+ 
                          || SSH 
                          || Tunnel 
                          \/ 
                     +-------------+ 
                     | Remote Host | 
                     | (api-serv)  |
                     +-------------+
```

Этот пример можно вставить в ваш `README.md` для иллюстрации структуры системы. Здесь:

- "Client (FastAPI)" — это сервер, на котором запущен ваш FastAPI контейнер.
- "Remote Host (api-serv)" — это удаленный сервер, к которому вы устанавливаете SSH туннель.
  
## Основные акценты настройки:

1. **FastAPI**: Запуск контейнера на клиенте.
2. **SSH Tunnel**: Установка SSH-туннеля между клиентом и удаленным сервером.
3. **UFW Rules**: Настройка правил файервола на удаленном сервере.
4. **Cron Job**: Установка Cron Job для автоматического выполнения скрипта `check_ssh_tunnel.sh`.

В каждом из этих частей можно углубиться, предоставляя дополнительные инструкции и пояснения.
