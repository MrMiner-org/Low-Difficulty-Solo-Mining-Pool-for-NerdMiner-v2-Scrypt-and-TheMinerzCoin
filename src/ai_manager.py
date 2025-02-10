import time
from ai.ai_core import AICore
from utils.logger import log

class AIManager:
    def __init__(self):
        self.ai_core = AICore()

    def run_cycle(self):
        while True:
            log("Running AI optimization cycle...")
            self.ai_core.optimize_pool()
            self.ai_core.predict_rewards()
            time.sleep(3600)
