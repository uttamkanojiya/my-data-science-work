from flask import Flask,render_template,flash

app = Flask(__name__)

app.secret_key = 'mysecret'

@app.route('/')
def index():
    flash("Welcome to my Home Page.")
    return render_template('index.html')

@app.route('/about')
def about():
    flash("Welcome to my About Page.")
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)