from utils.logger import log
from src.stratum import StratumServer

class Pool:
    def __init__(self):
        self.stratum_server = StratumServer()

    def start(self):
        log("Pool logic started. Waiting for miner connections...")
        self.stratum_server.start()
