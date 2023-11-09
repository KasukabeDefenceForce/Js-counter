from collections import defaultdict
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/counter")
def counter():
    return render_template("layout.html")


@app.route("/additionform", methods=["GET", "POST"])
def additionform():
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        sum = int(num1) + int(num2)
        return render_template("output.html", sum=sum, num1=num1, num2=num2)
    return render_template("additionForm.html")


@app.route("/textform", methods=["GET", "POST"])
def textform():
    errors = defaultdict(list)

    def checkNumber(x):
        try:
            return int(x)
        except ValueError:
            return None

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        if name == "":
            errors["name"].append("Name cannot be empty")
        elif not name[0].isalpha():
            errors["name"].append(
                "Name cannot start with a number or a special character"
            )

        if checkNumber(phone) == None:
            errors["phone"].append("Enter a valid number")
        elif int(phone) <= 0:
            errors["phone"].append("Phone cannot be a negative number or zero")
        if email == "":
            errors["email"].append("Email cannot be empty")
        elif email[0].isupper():
            errors["email"].append("Email cannot start with a capital letter")
        elif not email[0].isalpha():
            errors["email"].append(
                "Email cannot start with a number or a special character"
            )
        if not errors:
            return render_template(
                "information.html", name=name, phone=phone, email=email
            )
    return render_template("textForm.html", errors=errors)
