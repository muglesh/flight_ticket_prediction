from flask import Flask,request,jsonify
import util
app= Flask(__name__)
@app.route('/hello')
def hello():
    return "Hi"
@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        "locations":util.get_location_names()
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response
@app.route('/predict_flight_price',methods=['POST'])
def predict_flight_price():
    airline=str(request.form['airline'])
    Class=str(request.form['Class'])
    destination=str(request.form['destination'])
    departure=str(request.form['departure'])
    day=str(request.form['day'])
    stops =str(request.form['stops'])

    response=jsonify({
        'estimated_price':util.get_estimated_price(airline,Class,destination,departure,day,stops)
    })

    response.headers.add('Access-control-Allow-Origin','*')

    return response

if __name__== "__main__":
    print("starting python flask server for prediction....")
    app.run()