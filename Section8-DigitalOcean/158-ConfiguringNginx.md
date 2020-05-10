# Configuring Nginx
* ```sudo apt install nginx```
* Lets check our firewall: ```sudo ufw status```, it is inactive. We are going to enable it later on, to keep us safe.
* Before enabling firewall, we have to allow Nginx HTTP ```sudo ufw allow 'Nginx HTTP'```, so that we will be able to acess Nginx from the outside world, make requests to our application, and we also have to allow SSH, so that we can stay logged in when we enable the firewall: ```sudo ufw allow ssh```. Next we are going to do  ```sudo ufw enable```.
* Next we do ```sudo systemctl status nginx```, to check if it is active and running. If not, instad of status, you could do start, stop or reload.
* Now let's configure nginx for our application: ```sudo vi /etc/nginx/sites-available/pricing-service.conf```. This will bring an empty file, where we're gonna define how Nginx is going to behave in this context. Nginx works by defining different server blocks and each server block is completly independent and runs 100% of the time. The code of definitions follows:
```
server{
    listen 80;
    real_ip_header X-Forwarded-For;
    set_real_ip_from 127.0.0.1;
    server_name localhost;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/var/www/html/pricing-service/socket.sock;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```
* This server, or all the code that we included inside this server block, will happen when a user makes a request on port 80. Port 80 is the default port for HTTP requests, so whenever somebody acesses our server's address this block will run.
* After saving the file, do ```sudo rm /etc/nginx/sites-enabled/default``` to remove the default server that's already there.
* Then, ```sudo ln -s /etc/nginx/sites-available/pricing-service.conf /etc/nginx/sites-enabled/```.
* Then ```sudo systemctl reload nginx``` and then  ```sudo systemctl start uwsgi_pricing_service```
* It is working!!!