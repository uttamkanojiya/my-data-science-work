from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    lang = request.args.get('lang')
    return render_template('index.html',name=name,lang=lang)

if __name__ == '__main__':
    app.run(debug=True,port=4000)