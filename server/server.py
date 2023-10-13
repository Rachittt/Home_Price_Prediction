from flask import Flask, request, jsonify
import util

app = Flask(__name__)


# @app.route('/get_location_names', methods=['GET'])
@app.route('/get_location_and_area', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names(),
        'area_type': util.get_area_types()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    bhk = int(request.form['bhk'])
    area_type = request.form['area_type']
    location = request.form['location']

    response = jsonify({
        'estimated_price': util.get_estimated_price(total_sqft, bath, balcony, bhk, area_type, location)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__=="__main__":
    print("Starting Pyhton Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()