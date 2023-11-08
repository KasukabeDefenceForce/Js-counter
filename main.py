from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/counter")
def counter():
    return render_template("layout.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        sum = int(num1) + int(num2)
        return render_template("output.html", sum=sum, num1=num1, num2=num2)
    return render_template("form.html")
