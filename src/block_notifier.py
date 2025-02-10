from utils.logger import log
from utils.notifier import Notifier

def notify_block_found(miner_id, block_hash):
    message = f"🎉 New block found by miner {miner_id}: {block_hash} 🎉"
    log(message)
    notifier = Notifier()
    notifier.send_discord_notification(message)
    notifier.send_telegram_notification(message)

class BlockNotifier:
    def monitor(self):
        import time
        while True:
            # Simulation: Alle 30 Sekunden ein Blockfund
            time.sleep(30)
            notify_block_found("Miner123", "0000000000ABCDEF")
