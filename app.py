from flask import Flask, request, jsonify
from neo4j import GraphDatabase
from config import Config


app = Flask(__name__)

# Initialize Neo4j Driver
driver = GraphDatabase.driver(Config.NEO4J_URI, auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD))

# Close driver connection when app terminates
@app.teardown_appcontext
def close_driver(error):
    driver.close()


# Utility function to run queries
def run_query(query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters or {})
        return [record.data() for record in result]


# Example route: Create a person node
@app.route('/create_person', methods=['POST'])
def create_person():
    data = request.json
    query = """
    CREATE (p:Person {name: $name, age: $age, occupation: $occupation})
    RETURN p
    """
    parameters = {
        'name': data['name'],
        'age': data['age'],
        'occupation': data['occupation']
    }
    result = run_query(query, parameters)
    return jsonify(result)


# Example route: Retrieve all persons
@app.route('/persons', methods=['GET'])
def get_persons():
    query = "MATCH (p:Person) RETURN p"
    result = run_query(query)
    return jsonify(result)


@app.route('/person/<name>/relationships', methods=['GET'])
def get_person_relationships(name):
    query = """
    MATCH (p:Person {name: $name})-[r]->(related)
    RETURN type(r) AS relationship, related.name AS related_person
    """
    parameters = {'name': name}
    result = run_query(query, parameters)
    return jsonify(result)


# Example route: Find a person by name
@app.route('/person/<name>', methods=['GET'])
def get_person_by_name(name):
    query = "MATCH (p:Person {name: $name}) RETURN p"
    parameters = {'name': name}
    result = run_query(query, parameters)
    return jsonify(result)


# Example route: Update a person's occupation
@app.route('/update_person/<name>', methods=['PUT'])
def update_person(name):
    data = request.json
    query = """
    MATCH (p:Person {name: $name})
    SET p.occupation = $occupation
    RETURN p
    """
    parameters = {'name': name, 'occupation': data['occupation']}
    result = run_query(query, parameters)
    return jsonify(result)


# Example route: Delete a person
@app.route('/delete_person/<name>', methods=['DELETE'])
def delete_person(name):
    query = "MATCH (p:Person {name: $name}) DELETE p"
    parameters = {'name': name}
    run_query(query, parameters)
    return jsonify({"message": f"Person {name} deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
