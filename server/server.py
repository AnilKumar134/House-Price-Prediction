from flask import Flask, request, jsonify
import util  # import your util.py module

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names_endpoint():
    try:
        response = jsonify({
            'locations': util.get_location_names()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        # Get form data
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        # Get predicted price using util.py
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        # Return response
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Load model and columns from util.py
    app.run(debug=True)
