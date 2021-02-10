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
4. Run this command to use Docker without root privileges `sudo usermod -aG docker admin`

## Install and run containers
Run the following commands to install and run the three containers:
- `docker run -d -p 8050:8050 --name=dashboard_italy alex27riva/dash_italy`
  
- `docker run -d -p 8051:8050 --name=dashboad_lomb alex27riva/dashboard_lombardia`
  
- `docker run -d -p 8052:8050 --name=dashboard_regioni alex27riva/dashboard_regioni`

## Easy container management
For an easy container administration you can install Portnainer
Run these two commands:
1. `docker volume create portainer_data`
2.  `docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce`

Now you can easily manage your container throughout a web page at http://<ip-address>:9000

## Container port configuration
| Name | Internal port | External port |
| --- | --- | --- |
| Dashboard Italia | 8050 | 8050 |
| Dashboard Lombardia | 8050 | 8051 |
| Dashboard Regioni | 8050 | 8052 |