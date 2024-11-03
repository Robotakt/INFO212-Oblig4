# Initialize an empty dictionary to store customer information
customers = {}

# Function to create a new customer entry
def create_customer(customer_id, name, age, address):
    customers[customer_id] = {
        "name": name,
        "age": age,
        "address": address
    }
    print(f"Customer with ID {customer_id} created successfully.")

# Function to read a customer entry by their ID
def read_customer(customer_id):
    if customer_id in customers:
        print(f"Details for Customer ID {customer_id}:")
        for key, value in customers[customer_id].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"Customer with ID {customer_id} not found.")

# Function to update a customer entry
def update_customer(customer_id, name=None, age=None, address=None):
    if customer_id in customers:
        if name:
            customers[customer_id]["name"] = name
        if age:
            customers[customer_id]["age"] = age
        if address:
            customers[customer_id]["address"] = address
        print(f"Customer with ID {customer_id} updated successfully.")
    else:
        print(f"Customer with ID {customer_id} not found.")

# Function to delete a customer entry
def delete_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        print(f"Customer with ID {customer_id} deleted successfully.")
    else:
        print(f"Customer with ID {customer_id} not found.")