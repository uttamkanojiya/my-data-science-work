from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form["email"]
        passoword = request.form["password"]
        print(f"The name is {name} and the password is {passoword}")
        return "<b>Thanks for logging In.</b>"
    return render_template('index.html')

app.run(debug=True)
