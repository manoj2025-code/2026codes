from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 3.0
    elif units <= 200:
        bill = (100 * 3.0) + (units - 100) * 4.5
    elif units <= 300:
        bill = (100 * 3.0) + (100 * 4.5) + (units - 200) * 6.0
    else:
        bill = (100 * 3.0) + (100 * 4.5) + (100 * 6.0) + (units - 300) * 7.5

    fixed_charge = 50
    return round(bill + fixed_charge, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    bill_amount = None
    units = None

    if request.method == "POST":
        units = float(request.form["units"])
        bill_amount = calculate_bill(units)

    return render_template("index.html", bill=bill_amount, units=units)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)

