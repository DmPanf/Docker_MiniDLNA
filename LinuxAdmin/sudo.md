The error messages indicate that `sudo` is trying to prompt for a password but can't because there's no terminal available. This is common when running `sudo` in a script or background process.

Here are some ways to resolve this:

1. **SSH Config**: If the `sudo` commands are being run on a remote server, you can configure SSH to allocate a pseudo-terminal for that session. Add the `-t` flag to your SSH command, like so:

    ```bash
    ssh -t -p ${SSH_PORT} ${REMOTE_USER_SERVER} 'sudo ufw allow ${REMOTE_PORT}/tcp'
    ```

    Note that this might not work well in an automated script without human interaction.

2. **NOPASSWD**: You could configure `sudo` to allow the specific command to run without requiring a password. Edit the sudoers file (`sudo visudo`), and add a line like:

    ```
    username ALL=(ALL) NOPASSWD: /full/path/to/command
    ```

    Replace `username` with your username and `/full/path/to/command` with the command you want to run without a password.

    **Warning**: Use `NOPASSWD` carefully, as it can create security risks.

3. **Environment Variables and askpass**: You could set an environment variable `SUDO_ASKPASS` to a script that will supply the password to `sudo`. Then you can run `sudo -A`:

    ```bash
    export SUDO_ASKPASS="/path/to/script_returning_password"
    sudo -A your_command_here
    ```

    Your password script (`/path/to/script_returning_password`) should be something like:

    ```bash
    #!/bin/bash
    echo "mysecretpassword"
    ```

    Make sure this script is well-protected, as storing passwords in plaintext is a security risk.

Choose the method that best fits your security and usability requirements.
