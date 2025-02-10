# Low-Difficulty Solo Mining Pool for NerdMiner v2 Scrypt and TheMinerzCoin

This project provides a cutting-edge solo mining pool for Scrypt-based coins, optimized for NerdMiner v2 devices and TheMinerzCoin (TMC).

## Features

- **AI Automation:**  
  Self-learning AI continuously optimizes pool parameters and dynamically adjusts settings for optimal performance.

- **Real-Time Dashboard:**  
  Live statistics with interactive graphs, Dark Mode, and multi-language support (English, German, Spanish).

- **Admin Dashboard:**  
  Full configuration management including secure login (with optional 2FA, IP-whitelisting, and rate limiting), logging, and system monitoring.

- **Weekly Leaderboard Rewards:**  
  Automated payouts for the top 3 miners:
  - **1st Place:** 200 TMC
  - **2nd Place:** 100 TMC
  - **3rd Place:** 50 TMC

- **Notifications:**  
  Discord and Telegram alerts are sent automatically when a new block is found.

- **Security:**  
  Data encryption, SSL/TLS via Certbot, robust logging, and advanced security measures (e.g., rate limiting).

- **Community Features:**  
  Referral system, competitions, and gamification elements to enhance user engagement.

- **Performance & Analytics:**  
  Mining pattern analysis, anomaly detection, energy efficiency calculations, and a green mining dashboard to visualize energy consumption and savings.

## Installation

### Requirements
- Ubuntu 20.04, 22.04, or 24.04 / Debian 11, 12
- Python 3.8+
- MariaDB/MySQL, Redis, Nginx, Certbot

### Steps to Install

1. **Clone the Repository:**
   ```
   git clone https://github.com/MrMiner-org/Low-Difficulty-Solo-Mining-Pool-for-NerdMiner-v2-Scrypt-and-TheMinerzCoin.git
   cd Low-Difficulty-Solo-Mining-Pool-for-NerdMiner-v2-Scrypt-and-TheMinerzCoin
	```
2. **Run the Installation Script (do not run as root):**
   ```bash install.sh
   ```
   The script will:

  -  Update the system and install dependencies.
  -  Set up a Python virtual environment and install Python packages.
  -  Configure the database.
  -  Interactively create an admin account for the Admin Dashboard.
  -  Set up SSL using Certbot and configure Nginx for HTTPS.
  -  Configure the UFW firewall.
  
3. **Start the Pool:**
   ```
   python3 src/main.py
   ```
   
## Update Process

To update the pool software, run:
   ```
   python3 utils/update_script.py
   ```
   This script fetches the latest changes from the GitHub repository and applies them automatically.
   
## NerdMiner Firmware
For Scrypt mining, use the NerdMiner v2 Scrypt Firmware see https://github.com/ek0onsec/NerdMiner_v2_Scrypt

## License

This project is released under the terms of the MIT license. See [COPYING](COPYING) for more
information or see https://opensource.org/licenses/MIT.