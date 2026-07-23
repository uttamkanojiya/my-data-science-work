from flask import Flask,render_template,flash

app = Flask(__name__)

app.secret_key = 'badass'

value = True

@app.route('/')
def index():
    if value is True:
        flash('this is flashed message', 'info')
    return render_template('index.htm')

@app.route('/about')
def about():
    if value is True:
        flash('this is flashed message', 'info')
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
