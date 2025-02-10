import threading
import socket
import ssl
import json
from utils.logger import log
from utils.config_loader import load_config
from src.block_notifier import notify_block_found

class StratumServer:
    def __init__(self):
        config = load_config()
        self.host = config["stratum"]["host"]
        self.port = config["stratum"]["port"]
        self.ssl_enabled = config["stratum"]["ssl"]
        self.cert = config["stratum"]["cert"]
        self.key = config["stratum"]["key"]

    def start(self):
        log("Starting Stratum server...")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        log(f"Stratum server listening on {self.host}:{self.port}")

        if self.ssl_enabled:
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile=self.cert, keyfile=self.key)
        else:
            context = None

        while True:
            client_socket, addr = server_socket.accept()
            log(f"New connection from {addr}")
            if context:
                try:
                    client_socket = context.wrap_socket(client_socket, server_side=True)
                except Exception as e:
                    log(f"SSL error: {e}")
                    client_socket.close()
                    continue
            threading.Thread(target=self.handle_client, args=(client_socket, addr)).start()

    def handle_client(self, client_socket, addr):
        try:
            data = client_socket.recv(1024).decode("utf-8")
            request = json.loads(data)
            if request.get("action") == "submit_share" and request.get("valid"):
                miner_id = request.get("miner_id")
                block_hash = request.get("block_hash")
                notify_block_found(miner_id, block_hash)
                client_socket.sendall(json.dumps({"status": "accepted"}).encode("utf-8"))
            else:
                client_socket.sendall(json.dumps({"status": "rejected"}).encode("utf-8"))
        except Exception as e:
            log(f"Error handling client {addr}: {e}")
        finally:
            client_socket.close()

    def monitor_shares(self):
        # Dummy loop to simulate monitoring shares
        import time
        while True:
            log("Monitoring miner shares...")
            time.sleep(5)
