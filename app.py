from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime

app = Flask(__name__)

LOCATION_FILE = "location_log.json"

# 首頁直接開地圖
@app.route("/")
def index():
    return render_template("map.html")

@app.route("/driver")
def driver():
    return render_template("driver.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

# 手機 POST GPS
@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    if "lat" in data and "lon" in data:
        data["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOCATION_FILE, "w") as f:
            json.dump(data, f)
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"}), 400

# 供地圖 fetch 最新位置
@app.route("/latest")
def latest():
    if os.path.exists(LOCATION_FILE):
        with open(LOCATION_FILE) as f:
            data = json.load(f)
        return jsonify(data)
    else:
        # 如果沒有位置，回傳預設座標
        return jsonify({
            "lat": 25.0330,
            "lon": 121.5654,
            "time": ""
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




