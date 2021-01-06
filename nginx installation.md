# Nginx reverse proxy on Ubuntu Server

## Installation

1. `apt update`
2. `apt install nginx`
3. `unlink /etc/nginx/sites-enabled/default`
4. sudo nano /etc/nginx/sites-available/reverse-proxy.conf

Enter the following configuration:

```

server {
        listen 80;
        listen 443;
        listen [::]:80;
        ssl on;
        ssl_certificate /etc/letsencrypt/live/dash.covid19-italy.it/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/dash.covid19-italy.it/privkey.pem;
```

        server_name dash.covid19-italy.it
    
        access_log /var/log/nginx/reverse-access.log;
        error_log /var/log/nginx/reverse-error.log;
    
        location /italy/ {
                    proxy_pass http://localhost:8050;

  }

        location /lombardy/ {
                proxy_pass http://localhost:8051;

 }

        location /regions/ {
                proxy_pass http://localhost:8052;

 }
}



6. ```
   ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
   
   ```

7.  Test configuration: 
   
   ```
   nginx -t
   ```



## Install SSL certfificate



1. Check if snap is updated `sudo snap install core; sudo snap refresh core`

2. Install Certbot `sudo snap install --classic certbot`

3. Make simbolic link for the binary`sudo ln -s /snap/bin/certbot /usr/bin/certbot`

4. Get the certificate `sudo certbot --nginx`



In case of unsuccessful installation, the certificate will be saved in:

- certificate: `/etc/letsencrypt/live/{DOMAIN}/fullchain.pem`

- Private key: `/etc/letsencrypt/live/{DOMAIN}/privkey.pem`



## Final step

Restart Nginx server with 
