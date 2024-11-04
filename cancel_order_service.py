# cancel_order_service.py
from customer import customers  # Import customers dictionary from customer.py
from cars import cars           # Import cars dictionary from cars.py
from order_car_service import orders  # Import orders dictionary from order_car_service.py

def cancel_order_car(customer_id, car_id):
    # Check if customer exists
    if customer_id not in customers:
        return {"error": f"Customer with ID {customer_id} does not exist."}, 404
    # Check if car exists
    if car_id not in cars:
        return {"error": f"Car with ID {car_id} does not exist."}, 404

    # Check if the customer has booked the specified car
    for order_id, order in orders.items():
        if order["customer_id"] == customer_id and order["car_id"] == car_id and order["status"] == "booked":
            # Update the order and car status
            order["status"] = "cancelled"
            cars[car_id]["status"] = "available"
            return {"message": f"Booking cancelled successfully for Order ID {order_id}."}, 200

    # If no matching booking is found
    return {"error": f"No active booking found for Customer ID {customer_id} and Car ID {car_id}."}, 400
