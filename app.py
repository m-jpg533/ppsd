from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running successfully on Render!"

@app.route("/driver")
def driver():
    return render_template("driver.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/latest")
def latest():
    return jsonify({
        "lat": 25.0330,
        "lon": 121.5654
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
