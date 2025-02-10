from flask import Flask, render_template, request, redirect, url_for, session
from utils.config_loader import load_config
from utils.logger import log
from src.db.queries import get_leaderboard

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Bitte anpassen!

@app.route("/")
def index():
    # Öffentliche Startseite des Dashboards
    return render_template("index.html")

@app.route("/stats")
def stats():
    # Beispiel: Statistiken abrufen (hier Dummy-Daten)
    stats = {
        "active_miners": 15,
        "total_blocks": 120,
        "network_hashrate": "500 MH/s"
    }
    return render_template("stats.html", stats=stats)

@app.route("/leaderboard")
def leaderboard():
    # Leaderboard-Daten aus der Datenbank abrufen (hier Dummy-Daten)
    lb = get_leaderboard()
    return render_template("leaderboard.html", leaderboard=lb)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        # Konfiguration speichern (Platzhalter)
        log("Admin updated pool configuration.")
        return redirect(url_for("admin"))
    config = load_config()
    return render_template("admin.html", config=config)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Einfaches Admin-Login (Platzhalter)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Hier sollte die echte Überprüfung erfolgen
        if username == "admin" and password == "admin123":
            session["admin_logged_in"] = True
            return redirect(url_for("admin"))
        else:
            return "Invalid credentials", 401
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
