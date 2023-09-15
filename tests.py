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


def test_home():
    """
    Test the home endpoint of the API.

    This function sends a GET request to the home endpoint and checks if the response
    contains the expected content.

    Returns:
        None
    """
    url = 'http://localhost:5003'
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected content
    expected_content = """<h2>HNGx REST API</h2>
    <p>This is a simple REST API for the HNGx Internship at Zuri Team.<br>
    Add /api at the end of your URL.</p>
    """

    assert expected_content in response.text

    print("home endpoint test passed.")


def test_create_person(name):
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


def test_read_person(user_id):
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


def test_update_person(user_id, new_name):
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


def test_delete_person(user_id):
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


def test_read_all_persons():
    """
    Test the read_all_persons function of the API.

    This function sends a GET request to the read_all_persons endpoint and checks if the response
    contains the expected content.

    Returns:
        None
    """
    url = BASE_URL
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains data (a non-empty JSON array)
    assert len(response.json()) > 0

    print("read_all_persons endpoint test passed.")


# Run the main application and perform different tests
if __name__ == '__main__':
    try:
        # CREATE: Adding a new person
        create_response = test_create_person('Mark Essien')
        if create_response.status_code == 201:
            print('Person created successfully.')
        else:
            print('Error creating person:', create_response.status_code, create_response.json())

        # READ: Fetching details of a person
        user_id = 1  # Replace with the desired user ID
        get_response = test_read_person(user_id)
        if get_response.status_code == 200:
            person_data = get_response.json()
            print('Person Details:', person_data)
        else:
            print('Error getting person:', get_response.status_code, get_response.json())

        # UPDATE: Modifying details of an existing person
        update_response = test_update_person(user_id, 'Updated Name')
        if update_response.status_code == 200:
            print('Person updated successfully.')
        else:
            print('Error updating person:', update_response.status_code, update_response.json())

        # DELETE: Removing a person
        delete_response = test_delete_person(user_id)
        if delete_response.status_code == 204:
            print('Person deleted successfully.')
        else:
            print('Error deleting person:', delete_response.status_code, delete_response.json())

        # Test the home endpoint
        test_home()

        # Test the read_all_persons endpoint
        test_read_all_persons()

    except requests.exceptions.RequestException as error:
        print('Request Error:', error)
