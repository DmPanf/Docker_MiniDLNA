!#/bin/bash

sudo pamac install docker
sudo docker --version
sudo pamac install docker-compose
sudo systemctl enable --now docker.service
sudo systemctl status docker.service
sudo usermod -aG docker $USER
sudo docker info
docker-compose up -d
docker ps -a
docker logs -f
docker top minidlna
docker logs minidlna

# docker pull rustdesk/rustdesk-server:latest
