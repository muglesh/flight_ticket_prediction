from flask import Flask,  request, jsonify
import util as util
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hi"


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        "locations": util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_Class_names')
def get_class_names():
    response = jsonify({

        "Class": util.get_class_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_airline_names')
def get_airline_names():
    response = jsonify({

        "airlines": util.get_airline_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_flight_price', methods=['POST'])
def predict_flight_price():
    airline = str(request.form['airline'])
    Class = int(request.form['Class'])
    destination = str(request.form['destination'])
    departure = str(request.form['departure'])
    day = str(request.form['day'])
    stops = int(request.form['stops'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(airline, Class, destination, departure, day, stops)
    })

    response.headers.add('Access-control-Allow-Origin', '*')

    return response


