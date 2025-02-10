import subprocess
import sys
import os
from utils.logger import log

def check_for_updates():
    log("Checking for updates from GitHub repository...")
    # Sicherstellen, dass wir im richtigen Verzeichnis sind
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_dir)
    try:
        # Git-Pull ausführen, um Updates zu holen
        result = subprocess.run(["git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            log("Update successful:")
            log(result.stdout)
        else:
            log("Update failed:")
            log(result.stderr)
    except Exception as e:
        log(f"An error occurred during update: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_for_updates()