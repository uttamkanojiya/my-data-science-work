"""
from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {"data":1000,"Prediction":98.12}
    return jsonify(data),200

if __name__ == '__main__':
    app.run(debug=True,port=9149)
"""  #Created By Me!

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/predict', methods=['GET'])
def predict():
    value = request.args.get('value')
    
    if value is None:
        return jsonify({'error': 'Missing input'}), 400

    # Simulated prediction (replace with actual model call)
    result = int(value) * 2

    return jsonify({
        'input': value,
        'prediction': result
    })

if __name__ == '__main__':
    app.run(debug=True, port=9149)