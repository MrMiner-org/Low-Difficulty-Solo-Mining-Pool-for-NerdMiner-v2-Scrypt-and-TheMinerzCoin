import json

def load_config():
    with open("config/config.json", "r") as f:
        return json.load(f)
