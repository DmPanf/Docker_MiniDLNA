import json
import time
import os
import subprocess

FILE_PATH = '/path/to/your/file.json'
ALLOWED_SERVICES = ['nginx', 'redis', 'custom_script']
ALLOWED_ACTIONS = ['start', 'stop', 'restart']

def execute_command(service, action):
    if service in ALLOWED_SERVICES and action in ALLOWED_ACTIONS:
        # Выполнение команды для управления службой, например через systemctl
        cmd = f'sudo systemctl {action} {service}'
        subprocess.run(cmd, shell=True)
        print(f'{action}ing {service}')
    else:
        print(f'Invalid service or action for {service}: {action}')

def poll_file():
    while True:
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'r') as file:
                commands = json.load(file)
                for service, action in commands.items():
                    execute_command(service, action)
            
            # Очистка файла после выполнения команд
            open(FILE_PATH, 'w').close()
        
        time.sleep(15)

if __name__ == "__main__":
    poll_file()
