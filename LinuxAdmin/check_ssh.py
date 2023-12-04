#!/bin/bash
# [Created]: 03-09-2023
# [Last Modified]: 05-09-2023
# [File]: /home/bunta/scr/check_ssh_tunnel.sh
# [Crontab]: */3 * * * *  /home/bunta/scr/check_ssh_tunnel.sh
# [Description]: This script checks if the SSH tunnel and FastAPI container are running and takes appropriate actions.
# [Author]: Dmitrii [https://github.com/dmpanf]
# [Dependencies]: ssh, ps, docker, grep, pkill


# Initialize constants
REMOTE_PORT="8001"
LOCAL_PORT="8001"
REMOTE_USER_SERVER="bunta@api-serv.ru"

# Check if constants are set
if [[ -z "$REMOTE_PORT" || -z "$LOCAL_PORT" || -z "$REMOTE_USER_SERVER" ]]; then
    echo "Some constants are not set. Please provide them."
    read -p "Remote port: " REMOTE_PORT
    read -p "Local port: " LOCAL_PORT
    read -p "Remote user and server (user@server): " REMOTE_USER_SERVER
fi


# Function to check and set ufw rule on the remote server
check_and_set_ufw_rule() {
    isUfwRule=$(ssh -p 53217 bunta@api-serv.ru -i /home/bunta/.ssh/id_ed25519.vps1-ru 'sudo ufw status | grep 8001/tcp')
    if [[ ! $isUfwRule ]]; then
        ssh -p 53217 bunta@api-serv.ru -i /home/bunta/.ssh/id_ed25519.vps1-ru 'sudo ufw allow 8001/tcp'
    fi
}

# Function to check and set crontab entry
check_and_set_crontab() {
    isCronJob=$(crontab -l | grep '/home/bunta/scr/check_ssh_tunnel.sh')
    if [[ ! $isCronJob ]]; then
        (crontab -l ; echo "*/3 * * * * /home/bunta/scr/check_ssh_tunnel.sh") | crontab -
    fi
}

# Call the above functions
check_and_set_ufw_rule
check_and_set_crontab

# Check if the SSH daemon is running
isSSH=$(ps -ef | grep "[s]sh.*${REMOTE_PORT}:localhost:${LOCAL_PORT}")

# Check if the FastAPI Docker container is running
isFastAPI=$(docker ps --filter "ancestor=000-fastapi_app" --filter "status=running" | grep "0.0.0.0:${LOCAL_PORT}->${LOCAL_PORT}/tcp")

# If FastAPI is running but SSH tunnel is not, establish the SSH tunnel
if [[ $isFastAPI && ! $isSSH ]]; then
    ssh -f -N -R ${REMOTE_PORT}:localhost:${LOCAL_PORT} -p 53217 ${REMOTE_USER_SERVER} -i /home/bunta/.ssh/id_ed25519.vps1-ru
    echo "✅ SSH tunnel established" | wall
# If SSH tunnel is running but FastAPI is not, kill the SSH session
elif [[ $isSSH && ! $isFastAPI ]]; then
    pkill -f "ssh -f -N -R ${REMOTE_PORT}:localhost:${LOCAL_PORT} -p 53217 ${REMOTE_USER_SERVER} -i /home/bunta/.ssh/id_ed25519.vps1-ru"
    echo "❌ SSH tunnel terminated" | wall
fi
