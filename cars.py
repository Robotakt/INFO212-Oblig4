# Initialize an empty dictionary to store car information
cars = {}

# Function to create a new car entry
def create_car(car_id, make, model, year, location, status):
    cars[car_id] = {
        "make": make,
        "model": model,
        "year": year,
        "location": location,
        "status": status
    }
    print(f"Car with ID {car_id} created successfully.")

# Function to read a car entry by its ID
def read_car(car_id):
    if car_id in cars:
        print(f"Details for Car ID {car_id}:")
        for key, value in cars[car_id].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"Car with ID {car_id} not found.")

# Function to update a car entry
def update_car(car_id, make=None, model=None, year=None, location=None, status=None):
    if car_id in cars:
        if make:
            cars[car_id]["make"] = make
        if model:
            cars[car_id]["model"] = model
        if year:
            cars[car_id]["year"] = year
        if location:
            cars[car_id]["location"] = location
        if status:
            cars[car_id]["status"] = status
        print(f"Car with ID {car_id} updated successfully.")
    else:
        print(f"Car with ID {car_id} not found.")

# Function to delete a car entry
def delete_car(car_id):
    if car_id in cars:
        del cars[car_id]
        print(f"Car with ID {car_id} deleted successfully.")
    else:
        print(f"Car with ID {car_id} not found.")