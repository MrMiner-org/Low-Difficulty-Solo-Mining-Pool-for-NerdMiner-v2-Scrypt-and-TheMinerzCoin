import mysql.connector
import json

def setup_database():
    with open("config/config.json", "r") as f:
        config = json.load(f)
    conn = mysql.connector.connect(
        host=config["database_host"],
        user="root",
        password=""
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database_name']}")
    conn.commit()
    cursor.close()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
