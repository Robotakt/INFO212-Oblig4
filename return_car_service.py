from customer import customers  # Import customers dictionary from customer.py
from cars import cars           # Import cars dictionary from cars.py
from order_car_service import orders  # Import orders dictionary from order_car_service.py

def return_car(customer_id, car_id, car_status):
    # Check if customer exists
    if customer_id not in customers:
        return {"error": f"Customer with ID {customer_id} does not exist."}, 404
    # Check if car exists
    if car_id not in cars:
        return {"error": f"Car with ID {car_id} does not exist."}, 404

    # Check if the customer has rented the specified car
    for order_id, order in orders.items():
        if order["customer_id"] == customer_id and order["car_id"] == car_id and order["status"] == "rented":
            # Update the order and car status based on the return condition
            order["status"] = "returned"
            if car_status == "ok":
                cars[car_id]["status"] = "available"
            elif car_status == "damaged":
                cars[car_id]["status"] = "damaged"
            else:
                return {"error": "Invalid car status provided. Use 'ok' or 'damaged'."}, 400
            
            return {"message": f"Car returned successfully for Order ID {order_id}. Car status: {cars[car_id]['status']}."}, 200

    # If no matching rental is found
    return {"error": f"No active rental found for Customer ID {customer_id} and Car ID {car_id}."}, 400
