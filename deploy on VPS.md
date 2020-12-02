# Deployment on a VPS
This is a short guide on how to deploy the three dashboard on a VPS using Docker.
## Requirements
VPS with a these minimum hardware specification:
- 1GB RAM
- 20GB disk space
- Ubuntu Server 20.04
- Root access

## Create admin account
1. Log in to your VPS as root `ssh root@<vps-ip-address>`
2. Make an account for the admin user `useradd -m admin`
3. Set a password for the admin account with `passwd admin`
4. Close the connection with the command `exit`

## Install Docker
1. Log in to your VPS with admin account `ssh admin@<vps-ip-address>`
2. Download the script for Docker `curl -fsSL https://get.docker.com -o get-docker.sh`
3. Execute the script `sudo sh get-docker.sh`
4. Run this command to use Docker without root privileges `sudo usermod -aG docker admin

## Build and run container
1. Clone the repository to the VPS.
2. `cd` into each dashboard folder
3. Build the container image `docker build -t <container-name>:latest .`
4. Run the container `docker run -d -p <ext-port>:8050 <id-container>`

## Container port configuration
| Name | Internal port | External port |
| --- | --- | --- |
| Dashboard Italia | 8050 | 8050 |
| Dashboard Lombardia | 8050 | 8051 |
| Dashboard Regioni | 8050 | 8052 |