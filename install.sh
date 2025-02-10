#!/bin/bash

# Prevent running as root
if [ "$EUID" -eq 0 ]; then
  echo "Please do not run this script as root. Create a new system user instead."
  echo "Example:"
  echo "sudo adduser pooluser"
  echo "sudo su - pooluser"
  exit 1
fi

echo "Starting installation process..."

# Update system and install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip mariadb-server redis-server nginx certbot python3-certbot-nginx git ufw

echo "Setting up Python virtual environment..."
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setting up database..."
python3 config/database_setup.py

echo "Creating admin account for Admin Dashboard..."
read -p "Enter admin username: " ADMIN_USERNAME
read -s -p "Enter admin password: " ADMIN_PASSWORD
echo
python3 src/admin_dashboard.py --create-admin --username "$ADMIN_USERNAME" --password "$ADMIN_PASSWORD"

echo "Setting up SSL with Certbot..."
read -p "Enter your domain name (e.g., example.com): " DOMAIN_NAME
sudo certbot certonly --standalone -d "$DOMAIN_NAME"
SSL_CERT="/etc/letsencrypt/live/$DOMAIN_NAME/fullchain.pem"
SSL_KEY="/etc/letsencrypt/live/$DOMAIN_NAME/privkey.pem"

echo "Configuring Nginx for SSL and reverse proxy..."
sudo bash -c "cat > /etc/nginx/sites-available/miningpool <<EOF
server {
    listen 80;
    server_name $DOMAIN_NAME;
    return 301 https://\$host\$request_uri;
}
server {
    listen 443 ssl;
    server_name $DOMAIN_NAME;
    ssl_certificate $SSL_CERT;
    ssl_certificate_key $SSL_KEY;
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF"
sudo ln -s /etc/nginx/sites-available/miningpool /etc/nginx/sites-enabled/
sudo systemctl restart nginx

echo "Configuring UFW firewall..."
sudo ufw allow 'Nginx Full'
sudo ufw enable

echo "Installation complete!"
echo "Start the pool with: python3 src/main.py"