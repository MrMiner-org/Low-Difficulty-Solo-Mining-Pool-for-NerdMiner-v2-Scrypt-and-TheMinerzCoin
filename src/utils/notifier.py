import requests
import json
from utils.logger import log

class Notifier:
    def __init__(self, config_path="config/config.json"):
        with open(config_path, "r") as f:
            config = json.load(f)
        self.discord_webhook = config.get("notifications", {}).get("discord_webhook")
        self.telegram_bot_token = config.get("notifications", {}).get("telegram_bot_token")
        self.telegram_chat_id = config.get("notifications", {}).get("telegram_chat_id")

    def send_discord_notification(self, message):
        if self.discord_webhook:
            payload = {"content": message}
            try:
                response = requests.post(self.discord_webhook, json=payload)
                if response.status_code == 204:
                    log("Discord notification sent successfully.")
                else:
                    log(f"Failed to send Discord notification: {response.status_code}")
            except Exception as e:
                log(f"Discord notification error: {e}")

    def send_telegram_notification(self, message):
        if self.telegram_bot_token and self.telegram_chat_id:
            url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
            payload = {"chat_id": self.telegram_chat_id, "text": message}
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    log("Telegram notification sent successfully.")
                else:
                    log(f"Failed to send Telegram notification: {response.status_code}")
            except Exception as e:
                log(f"Telegram notification error: {e}")
