# app.py
from flask import Flask, request, jsonify
from customer import customers  # Import customers dictionary from customer.py
from cars import cars           # Import cars dictionary from cars.py

app = Flask(__name__)

# Dictionary to store orders
orders = {}

# Endpoint to order a car
@app.route('/order-car', methods=['POST'])
def order_car():
    # Get JSON data from request
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")

    # Check if customer and car exist
    if customer_id not in customers:
        return jsonify({"error": f"Customer with ID {customer_id} does not exist."}), 404
    if car_id not in cars:
        return jsonify({"error": f"Car with ID {car_id} does not exist."}), 404

    # Check if car is available
    if cars[car_id]["status"] == "available":
        # Create the order
        order_id = len(orders) + 1  # Simple order ID generation
        orders[order_id] = {
            "customer_id": customer_id,
            "car_id": car_id,
            "status": "booked"
        }

        # Update car status to "booked"
        cars[car_id]["status"] = "booked"
        return jsonify({"message": f"Order created successfully!", "order_id": order_id}), 201
    else:
        return jsonify({"error": f"Car with ID {car_id} is not available for booking."}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)