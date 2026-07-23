from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Uttam"
    Lang = "Python"
    list1 = [1, 2, 3, 4, 5,131342,54,365,24,62,45,24,646426]
    return render_template('index.html',name=name,Lang=Lang,list1=list1)

app.run(debug=True)