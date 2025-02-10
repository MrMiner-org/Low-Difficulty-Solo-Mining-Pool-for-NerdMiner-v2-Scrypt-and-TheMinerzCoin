import argparse
from werkzeug.security import generate_password_hash
import mysql.connector
import json
import sys

def create_admin(username, password):
    with open("config/config.json", "r") as f:
        config = json.load(f)
    conn = mysql.connector.connect(
        host=config["database_host"],
        user=config["database_user"],
        password=config["database_password"],
        database=config["database_name"],
        port=config["database_port"]
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255)
        )
    """)
    hashed_password = generate_password_hash(password, method='sha256')
    cursor.execute("INSERT INTO admin_users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Admin account created successfully for username: {username}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--create-admin", action="store_true")
    parser.add_argument("--username", type=str, required=True)
    parser.add_argument("--password", type=str, required=True)
    args = parser.parse_args()
    if args.create_admin:
        create_admin(args.username, args.password)
