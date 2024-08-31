from flask import Flask, request, redirect, abort, url_for, render_template


import utils
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/convert/length', methods= ["GET", "POST"])
def convert_length():
    if request.method == "POST":

        amount = request.form['length-input']
        c_from = request.form['length-from']
        c_to = request.form['length-to']
        

        if amount == '':
            return  render_template("convert_weight.html", result="you have to enter the amount")

        result = utils.convert_length(amount, c_from, c_to)
        
        message=f"{amount} {c_from} = {result} {c_to}"
 
        return render_template("convert_length.html", result=message)
    
    return  render_template("convert_length.html")


@app.route('/convert/weight/', methods= ["GET", "POST"])
def convert_weight():

    if request.method == "POST":

        amount = request.form['weight-input']
        c_from = request.form['weight-from']
        c_to = request.form['weight-to']

        if amount == '':
            return  render_template("convert_weight.html", result="you have to enter the amount")

        result = utils.convert_mass(amount, c_from, c_to)
        
        message=f"{amount} {c_from} = {result} {c_to}"
 
        return render_template("convert_weight.html", result=message)
    
    return  render_template("convert_weight.html")


@app.route('/convert/temperature', methods= ["GET", "POST"])
def convert_temperature():
    if request.method == "POST":

        amount = request.form['temperature-input']
        c_from = request.form['temperature-from']
        c_to = request.form['temperature-to']

        if amount == '':
            return  render_template("convert_weight.html", result="you have to enter the amount")

        result = utils.convert_temperature(amount, c_from, c_to)
        
        message=f"{amount} {c_from} = {result} {c_to}"
 
        return render_template("convert_temp.html", result=message)
    
    return  render_template("convert_temp.html")


if __name__ == "__main__":
    app.run(debug=True)