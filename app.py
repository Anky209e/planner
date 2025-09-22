from flask import Flask, request, render_template, redirect, url_for
from src.planner import generate_plan
from src.db import init_db, save_plan, get_plan, get_history
import requests
app = Flask(__name__)

# init DB on startup
init_db()

def get_location_from_ip(ip=None):
    # Use ipinfo.io for free IP geolocation
    try:
        url = "https://ipinfo.io/json"
        if ip:
            url = f"https://ipinfo.io/{ip}/json"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        loc = data.get("loc", "0,0").split(",")
        return {"lat": float(loc[0]), "lon": float(loc[1])}
    except Exception:
        return {"lat": 0.0, "lon": 0.0}

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        goal = request.form.get("goal")
        # Get user's location from IP
        user_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
        location = get_location_from_ip(user_ip)
        plan_result = generate_plan(goal, location)
        pid = save_plan(goal, plan_result)
        return redirect(url_for("view_plan", plan_id=pid))
    return render_template("index.html")

@app.route("/plan/<int:plan_id>")
def view_plan(plan_id):
    p = get_plan(plan_id)
    if not p:
        return "Plan not found", 404
    return render_template("plan.html", plan=p)

@app.route("/history")
def history():
    hs = get_history()
    return render_template("history.html", plans=hs)

if __name__ == "__main__":
    app.run(debug=True)
