from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    result= ""
    
    if request.method=="POST":
        num1=float(request.form["n1"])
        num2=float(request.form["n2"])
        operation=request.form["operation"]

        if operation=="add":
            result=num1+num2

        elif operation=="sub":
            result=num1-num2

        elif operation=="mul":
            result=num1*num2

        elif operation=="div":
            result=num1/num2




    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)