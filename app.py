from flask import Flask, request, jsonify
from neo4j import GraphDatabase
from config import Config

app = Flask(__name__)
driver = GraphDatabase.driver(Config.NEO4J_URI, auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD))

@app.teardown_appcontext
def close_driver(error):
    driver.close()

def run_query(query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters or {})
        return [record.data() for record in result]

# CRUD for Cars
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    query = """
    CREATE (c:Car {make: $make, model: $model, year: $year, location: $location, status: $status})
    RETURN c
    """
    result = run_query(query, data)
    return jsonify(result), 201

@app.route('/cars', methods=['GET'])
def get_cars():
    query = "MATCH (c:Car) RETURN c"
    result = run_query(query)
    return jsonify(result)

@app.route('/cars/<car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.json
    query = """
    MATCH (c:Car) WHERE ID(c) = $car_id
    SET c += $data
    RETURN c
    """
    parameters = {"car_id": int(car_id), "data": data}
    result = run_query(query, parameters)
    return jsonify(result)

@app.route('/cars/<car_id>', methods=['DELETE'])
def delete_car(car_id):
    query = "MATCH (c:Car) WHERE ID(c) = $car_id DELETE c"
    parameters = {"car_id": int(car_id)}
    run_query(query, parameters)
    return jsonify({"message": "Car deleted"}), 204

# CRUD for Customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    query = "CREATE (c:Customer {name: $name, age: $age, address: $address}) RETURN c"
    result = run_query(query, data)
    return jsonify(result), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    query = "MATCH (c:Customer) RETURN c"
    result = run_query(query)
    return jsonify(result)

@app.route('/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.json
    query = "MATCH (c:Customer) WHERE ID(c) = $customer_id SET c += $data RETURN c"
    parameters = {"customer_id": int(customer_id), "data": data}
    result = run_query(query, parameters)
    return jsonify(result)

@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    query = "MATCH (c:Customer) WHERE ID(c) = $customer_id DELETE c"
    parameters = {"customer_id": int(customer_id)}
    run_query(query, parameters)
    return jsonify({"message": "Customer deleted"}), 204

# CRUD for Employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    query = "CREATE (e:Employee {name: $name, address: $address, branch: $branch}) RETURN e"
    result = run_query(query, data)
    return jsonify(result), 201

@app.route('/employees', methods=['GET'])
def get_employees():
    query = "MATCH (e:Employee) RETURN e"
    result = run_query(query)
    return jsonify(result)

@app.route('/employees/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    query = "MATCH (e:Employee) WHERE ID(e) = $employee_id SET e += $data RETURN e"
    parameters = {"employee_id": int(employee_id), "data": data}
    result = run_query(query, parameters)
    return jsonify(result)

@app.route('/employees/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    query = "MATCH (e:Employee) WHERE ID(e) = $employee_id DELETE e"
    parameters = {"employee_id": int(employee_id)}
    run_query(query, parameters)
    return jsonify({"message": "Employee deleted"}), 204

# Order a Car
@app.route('/order-car', methods=['POST'])
def order_car():
    data = request.json
    customer_id = data['customer_id']
    car_id = data['car_id']
    # Check that the customer has no other bookings
    check_query = "MATCH (cust:Customer)-[:BOOKED]->(:Car) WHERE ID(cust) = $customer_id RETURN cust"
    if run_query(check_query, {"customer_id": int(customer_id)}):
        return jsonify({"error": "Customer already has a booking"}), 400
    # Book the car
    query = """
    MATCH (cust:Customer), (car:Car)
    WHERE ID(cust) = $customer_id AND ID(car) = $car_id AND car.status = 'available'
    CREATE (cust)-[:BOOKED]->(car)
    SET car.status = 'booked'
    RETURN car
    """
    result = run_query(query, {"customer_id": int(customer_id), "car_id": int(car_id)})
    return jsonify(result)

# Cancel Order
@app.route('/cancel-order-car', methods=['POST'])
def cancel_order():
    data = request.json
    customer_id = data['customer_id']
    car_id = data['car_id']
    query = """
    MATCH (cust:Customer)-[r:BOOKED]->(car:Car)
    WHERE ID(cust) = $customer_id AND ID(car) = $car_id
    DELETE r
    SET car.status = 'available'
    RETURN car
    """
    result = run_query(query, {"customer_id": int(customer_id), "car_id": int(car_id)})
    return jsonify(result)

# Rent Car
@app.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.json
    customer_id = data['customer_id']
    car_id = data['car_id']
    query = """
    MATCH (cust:Customer)-[r:BOOKED]->(car:Car)
    WHERE ID(cust) = $customer_id AND ID(car) = $car_id
    DELETE r
    CREATE (cust)-[:RENTED]->(car)
    SET car.status = 'rented'
    RETURN car
    """
    result = run_query(query, {"customer_id": int(customer_id), "car_id": int(car_id)})
    return jsonify(result)

# Return Car
@app.route('/return-car', methods=['POST'])
def return_car():
    data = request.json
    customer_id = data['customer_id']
    car_id = data['car_id']
    status = data['status']  # 'available' or 'damaged'
    query = """
    MATCH (cust:Customer)-[r:RENTED]->(car:Car)
    WHERE ID(cust) = $customer_id AND ID(car) = $car_id
    DELETE r
    SET car.status = $status
    RETURN car
    """
    result = run_query(query, {"customer_id": int(customer_id), "car_id": int(car_id), "status": status})
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
