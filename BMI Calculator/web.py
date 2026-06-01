from flask import Flask, render_template, request

web = Flask(__name__)

@web.route("/")
def home():
    return render_template("bmi.html")

@web.route("/bmi", methods=["POST"])
def calculate_bmi():
    weight = float(request.form["weight"])
    height_cm = float(request.form["height"])
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    status = ""
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obesity"
    return render_template("bmi.html", bmi=round(bmi, 2), status=status, weight=weight, height_m=height_m)

if __name__ == "__main__":
    web.run(debug=True)