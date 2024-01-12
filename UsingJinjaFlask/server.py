from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", year=year)

if __name__ == "__main__":
    app.run(debug=True)
