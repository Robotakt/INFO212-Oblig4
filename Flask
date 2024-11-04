from flask import Flask, request, jsonify
from order_car_service import order_car  # Import the order_car function
from cancel_order_service import cancel_order_car  # Import the cancel_order_car function
from rent_car_service import rent_car  # Import the rent_car function
from return_car_service import return_car  # Import the return_car function

app = Flask(__name__)

# Endpoint to order a car
@app.route('/order-car', methods=['POST'])
def order_car_endpoint():
    # Get JSON data from request
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")

    # Call the order_car function and get the response
    response, status_code = order_car(customer_id, car_id)
    return jsonify(response), status_code

# Endpoint to cancel a car booking
@app.route('/cancel-order-car', methods=['POST'])
def cancel_order_car_endpoint():
    # Get JSON data from request
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")

    # Call the cancel_order_car function and get the response
    response, status_code = cancel_order_car(customer_id, car_id)
    return jsonify(response), status_code

# Endpoint to rent a car
@app.route('/rent-car', methods=['POST'])
def rent_car_endpoint():
    # Get JSON data from request
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")

    # Call the rent_car function and get the response
    response, status_code = rent_car(customer_id, car_id)
    return jsonify(response), status_code

# Endpoint to return a car
@app.route('/return-car', methods=['POST'])
def return_car_endpoint():
    # Get JSON data from request
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")
    car_status = data.get("car_status")  # Expecting 'ok' or 'damaged'

    # Call the return_car function and get the response
    response, status_code = return_car(customer_id, car_id, car_status)
    return jsonify(response), status_code

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
