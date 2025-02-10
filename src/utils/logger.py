import datetime

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = f"[{timestamp}] {message}"
    print(output)
    with open("logs/pool.log", "a") as f:
        f.write(output + "\n")
