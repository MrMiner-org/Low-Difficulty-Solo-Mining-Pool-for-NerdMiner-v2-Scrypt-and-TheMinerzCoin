import mysql.connector
from utils.config_loader import load_config

def get_db_connection():
    config = load_config()
    conn = mysql.connector.connect(
        host=config["database_host"],
        user=config["database_user"],
        password=config["database_password"],
        database=config["database_name"],
        port=config["database_port"]
    )
    return conn

def get_leaderboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT miner_id, username, shares, rewards FROM miners ORDER BY shares DESC LIMIT 10")
    leaderboard = cursor.fetchall()
    cursor.close()
    conn.close()
    result = {}
    for idx, entry in enumerate(leaderboard, start=1):
        result[idx] = entry
    return result
