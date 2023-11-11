import json

CONFIG_PATH = '/path/to/your/config.json'

def read_services():
    with open(CONFIG_PATH, 'r') as file:
        config = json.load(file)
        services = config.get("services", [])
        return services

if __name__ == "__main__":
    services = read_services()
    for service in services:
        print(service)
