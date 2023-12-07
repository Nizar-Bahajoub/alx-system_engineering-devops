#!/usr/bin/env bash
# Sets up web server for the deployment

if [ ! command -v nginx &>/dev/null ]; then
        sudo apt-get update
        sudo apt-get install -y nginx
fi

base_dir="/data/web_static/releases/test"
index_file="$base_dir/index.html"

for dir in "/data" "/data/web_static" "/data/web_static/releases" "/data/web_static/shared" "$base_dir"; do
        if [ ! -d "$dir" ]; then
                sudo mkdir -p "$dir"
        fi
done

echo "This is a Test !" | sudo tee "$index_file" > /dev/null

sudo chown -R ubuntu:ubuntu /data

if [ -L "/data/web_static/current" ]; then
        sudo rm -r "/data/web_static/current"
fi

sudo ln -s "$base_dir" "/data/web_static/current"

sudo echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By \$hostname;
        root /var/www/html;

        error_page 404 /custom_404.html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files  / =404;
        }

        location /redirect_me {
                rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }

        location /hbnb_static {
                alias /data/web_static/current;
        }
}" >  /etc/nginx/sites-available/default

sudo service nginx restart
