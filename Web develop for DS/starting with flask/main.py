from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/about')
def about_page():
    return "<p> This is an About page. </p>"

@app.route('/contact')
def contact_page():
    return "<p> this is an contact page. </p>"

@app.route('/home')
def home():
    return render_template("index.html")

app.run(debug=True)