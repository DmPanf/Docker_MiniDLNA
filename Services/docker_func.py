import docker

client = docker.from_env()

def start_container(container_name):
    container = client.containers.get(container_name)
    container.start()

def stop_container(container_name):
    container = client.containers.get(container_name)
    container.stop()

def restart_container(container_name):
    container = client.containers.get(container_name)
    container.restart()
