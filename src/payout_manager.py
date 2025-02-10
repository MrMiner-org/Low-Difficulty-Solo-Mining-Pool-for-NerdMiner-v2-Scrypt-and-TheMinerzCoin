import time
from datetime import datetime, timedelta
from utils.logger import log
from utils.config_loader import load_config

class PayoutManager:
    def __init__(self):
        self.last_payout = None

    def schedule_weekly_payouts(self):
        log("Starting weekly payout scheduler...")
        while True:
            now = datetime.now()
            if self.last_payout is None or now - self.last_payout >= timedelta(weeks=1):
                self.process_payouts()
                self.last_payout = now
            time.sleep(3600)

    def process_payouts(self):
        log("Processing weekly leaderboard rewards...")
        rewards = {1: 200, 2: 100, 3: 50}
        for rank, reward in rewards.items():
            log(f"Distributed {reward} TMC to miner at rank {rank}")
