from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    # For local dev only; Railway will use gunicorn via Procfile
    app.run(host="0.0.0.0", port=3000, debug=True)
