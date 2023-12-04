# SSH Tunnel & FastAPI Health Check

## System Architecture

Here is a simplified ASCII diagram illustrating the interaction between the local machine running a FastAPI instance and a remote server, connected through an SSH tunnel.

```
                     +---------------------+
                     |    Local Machine    |  
                     |     (FastAPI)       |
                     +----------+----------+ 
                            || SSH 
                            || Tunnel 
                            \/ 
                     +---------------------+ 
                     |    Remote Server    | 
                     |    (api-serv.ru)    |
                     +---------------------+
```

### Key Components

1. **Local Machine (FastAPI)**: This is where the FastAPI application runs inside a Docker container. It exposes port `8001` to interact with the SSH tunnel.

2. **SSH Tunnel**: An encrypted tunnel established between the local machine and the remote server. This is set up to forward traffic from a specified port on the remote server to a specified port on the local machine (FastAPI).

3. **Remote Server (api-serv.ru)**: This is the external server that listens on a specified port (`8001`). It receives incoming traffic and forwards it through the SSH tunnel to the FastAPI instance on the local machine.

## Configuration Highlights

### FastAPI Deployment

1. **Docker Setup**: Your FastAPI application should be containerized using Docker. Make sure the Docker daemon is running.
  
   ```
   docker-compose up -d
   ```
   
2. **Port Exposure**: Ensure that the FastAPI application inside the Docker container exposes the port you intend to tunnel (e.g., `8001`).

### SSH Tunnel Configuration

1. **SSH Key Pair**: If you haven't already, generate an SSH key pair for secure, password-less authentication to the remote server.
   
   ```
   ssh-keygen -t ed25519
   ```

2. **SSH Connection**: Use the SSH `-R` option to set up the reverse tunnel. Your script automates this.

   ```
   ssh -f -N -R 8001:localhost:8001 -p 53217 username@api-serv.ru -i ~/.ssh/id_ed25519
   ```
   
3. **Automate with Cron**: Your `check_ssh_tunnel.sh` script is set up to automatically establish the tunnel if it's not active. Add this script to your crontab to run it at regular intervals.
   
   ```
   crontab -e
   ```

### UFW Rules on Remote Server

1. **Install UFW**: If not already installed, you can install UFW on your Ubuntu server with:
   
   ```
   sudo apt-get install ufw
   ```
   
2. **Allow Port**: Open up the port (`8001` in this case) on UFW.

   ```
   sudo ufw allow 8001/tcp
   ```

3. **Enable UFW**: Finally, enable UFW with:

   ```
   sudo ufw enable
   ```

By following these steps, you ensure that the FastAPI application, the SSH tunnel, and the remote server are correctly configured to communicate with each other securely and reliably.
