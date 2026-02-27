from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run()