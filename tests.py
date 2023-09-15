"""
Python script using the requests library to test CRUD operations for the API.
The script performs these operations:
•	Add a new person (e.g., "Mark Essien").
•	Fetch details of a person
•	Modify the details of an existing person.
•	Remove a person
"""
import requests

# Base URL for the API
BASE_URL = 'http://localhost:5003/api'


def create_person(name):
    """
    Create a new person via a POST request to the API.

    Args:
        name (str): The name of the person to create.

    Returns:
        requests.Response: The response from the API.
    """
    url = BASE_URL
    data = {'name': name}
    response = requests.post(url, json=data)
    return response


def get_person(user_id):
    """
    Retrieve details of a person via a GET request to the API.

    Args:
        user_id (int): The ID of the person to retrieve.

    Returns:
        requests.Response: The response from the API.
    """
    url = f'{BASE_URL}/{user_id}'
    response = requests.get(url)
    return response


def update_person(user_id, new_name):
    """
    Update details of an existing person via a PUT request to the API.

    Args:
        user_id (int): The ID of the person to update.
        new_name (str): The new name for the person.

    Returns:
        requests.Response: The response from the API.
    """
    url = f'{BASE_URL}/{user_id}'
    data = {'name': new_name}
    response = requests.put(url, json=data)
    return response


def delete_person(user_id):
    """
    Delete a person via a DELETE request to the API.

    Args:
        user_id (int): The ID of the person to delete.

    Returns:
        requests.Response: The response from the API.
    """
    url = f'{BASE_URL}/{user_id}'
    response = requests.delete(url)
    return response


# Run the main application and perform different tests
if __name__ == '__main__':
    try:
        # CREATE: Adding a new person
        create_response = create_person('Mark Essien')
        if create_response.status_code == 201:
            print('Person created successfully.')
        else:
            print('Error creating person:', create_response.status_code, create_response.json())

        # READ: Fetching details of a person
        user_id = 1  # Replace with the desired user ID
        get_response = get_person(user_id)
        if get_response.status_code == 200:
            person_data = get_response.json()
            print('Person Details:', person_data)
        else:
            print('Error getting person:', get_response.status_code, get_response.json())

        # UPDATE: Modifying details of an existing person
        update_response = update_person(user_id, 'Updated Name')
        if update_response.status_code == 200:
            print('Person updated successfully.')
        else:
            print('Error updating person:', update_response.status_code, update_response.json())

        # DELETE: Removing a person
        delete_response = delete_person(user_id)
        if delete_response.status_code == 204:
            print('Person deleted successfully.')
        else:
            print('Error deleting person:', delete_response.status_code, delete_response.json())

    except requests.exceptions.RequestException as error:
        print('Request Error:', error)
