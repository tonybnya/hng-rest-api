"""
REST API capable of CRUD operations on a User Resource.

CREATE: Adding a new User -> /api
READ: Fetching details of a User -> /api/user_id
UPDATE: Modifying details of an existing User -> /api/user_id
DELETE: Removing a User -> /api/user_id
"""
from flask import Flask, request, jsonify, g
import sqlite3
import os

# Create a Flask application instance
app = Flask(__name__)

# Define the database file path
DATABASE = 'database.sqlite3'

# Check if the database file exists, and create it if not
if not os.path.exists('database.sqlite3'):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def get_db():
    """
    Get the SQLite database connection.

    This function creates a new connection if one does not exist for the current request context.

    Returns:
        sqlite3.Connection: The SQLite database connection.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_db(exception):
    """
    Close the SQLite database connection when the application context is turn down.

    Args:
        exception (Exception): Any exception that occurred during the request.
    """
    db = getattr(g, '_database', None)
    if db is not None:

        db.close()


@app.route('/api', methods=['POST'])
def create_person():
    """
    Create a new person resource.

    This route allows creating a new person by sending a POST request with JSON data.

    Returns:
        tuple: A tuple containing JSON response and HTTP status code.
    """
    try:
        # Get the 'name' from the request JSON data
        name = request.json['name']

        # Get the database connection
        db = get_db()
        cursor = db.cursor()

        # Insert the new person into the 'person' table
        cursor.execute('INSERT INTO person (name) VALUES (?)', (name,))
        db.commit()

        # Return a success response
        return jsonify({'message': 'Person created successfully'}), 201
    except Exception as error:
        # Return an error response with details
        return jsonify({'message': 'Error creating person', 'error': str(error)}), 500


@app.route('/api/<int:id>', methods=['GET'])
def get_person(id):
    """
    Retrieve details of a person by their ID.

    Args:
        id (int): The ID of the person to retrieve.

    Returns:
        tuple: A tuple containing JSON response and HTTP status code.
    """
    try:
        # Get the database connection
        db = get_db()
        cursor = db.cursor()

        # Query the database to retrieve the person with the given ID
        cursor.execute('SELECT * FROM person WHERE id = ?', (id,))
        person = cursor.fetchone()

        if person is None:
            # Return a not found response if the person does not exist
            return jsonify({'message': 'Person not found'}), 404

        # Return the person details
        return jsonify({'id': person[0], 'name': person[1]})
    except Exception as error:
        # Return an error response with details
        return jsonify({'message': 'Error getting person', 'error': str(error)}), 500


@app.route('/api/<int:id>', methods=['PUT'])
def update_person(id):
    """
    Update details of an existing person by their ID.

    Args:
        id (int): The ID of the person to update.

    Returns:
        tuple: A tuple containing JSON response and HTTP status code.
    """
    try:
        # Get the 'name' from the request JSON data
        name = request.json['name']

        # Get the database connection
        db = get_db()
        cursor = db.cursor()

        # Update the person's name in the 'person' table
        cursor.execute('UPDATE person SET name = ? WHERE id = ?', (name, id))
        db.commit()

        # Return a success response
        return jsonify({'message': 'Person updated successfully'}), 200
    except Exception as error:
        # Return an error response with details
        return jsonify({'message': 'Error updating person', 'error': str(error)}), 500


@app.route('/api/<int:id>', methods=['DELETE'])
def delete_person(id):
    """
    Delete a person by their ID.

    Args:
        id (int): The ID of the person to delete.

    Returns:
        tuple: A tuple containing JSON response and HTTP status code.
    """
    try:
        # Get the database connection
        db = get_db()
        cursor = db.cursor()

        # Delete the person from the 'person' table
        cursor.execute('DELETE FROM person WHERE id = ?', (id,))
        db.commit()

        # Return a success response
        return jsonify({'message': 'Person deleted successfully'}), 204
    except Exception as error:
        # Return an error response with details
        return jsonify({'message': 'Error deleting person', 'error': str(error)}), 500


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=5003)
