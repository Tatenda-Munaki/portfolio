from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    # must exist at templates/index.html
    return render_template("index.html")

# allows local run and cloud run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
