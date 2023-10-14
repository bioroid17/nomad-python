from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="nico")


@app.route("/search")
def search():
    return render_template("search.html", name="nico")


app.run("0.0.0.0")
