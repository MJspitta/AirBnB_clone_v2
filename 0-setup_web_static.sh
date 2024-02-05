#!/usr/bin/env bash
# set up web servers for deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    I am Madu Jang, a student of ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/hbnb_static/ {
    s/^#//
    s|root /var/www/html;|root /data/web_static/current/;|
    s|try_files $uri $uri/ =404;|try_files $uri $uri/ =404;|
    s|location /hbnb_static/ { alias /data/web_static/current/; }|location /hbnb_static/ { alias /data/web_static/current/; }|
}' /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
