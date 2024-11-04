# order_car_service.py
from customer import customers  # Import customers dictionary from customer.py
from cars import cars           # Import cars dictionary from cars.py

# Dictionary to store orders
orders = {}

def order_car(customer_id, car_id):
    # Check if customer and car exist
    if customer_id not in customers:
        return {"error": f"Customer with ID {customer_id} does not exist."}, 404
    if car_id not in cars:
        return {"error": f"Car with ID {car_id} does not exist."}, 404

    # Check if the customer has already booked a car
    for order in orders.values():
        if order["customer_id"] == customer_id and order["status"] == "booked":
            return {"error": f"Customer with ID {customer_id} has already booked a car."}, 400

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
        return {"message": f"Order created successfully!", "order_id": order_id}, 201
    else:
        return {"error": f"Car with ID {car_id} is not available for booking."}, 400