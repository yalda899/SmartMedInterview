# SmartMedInterview

Pet Store API Testing Project

This project provides automated tests for the Pet Store API, covering various test scenarios using Python, Pytest, and Requests. The test suite includes scenarios such as adding, updating, and deleting pets, as well as placing orders.

Prerequisites

1.    Python
Ensure Python (version 3.6 or later) is installed on your machine. You can check if Python is installed by running:

python --version

If Python is not installed, download it from python.org and follow the installation instructions.

2.    Pip
Pip (Python package installer) is usually included with Python installations. Verify it with:

pip --version

If pip is not installed, follow the installation instructions to add it.

Project Setup

1.    Clone the Project Repository
Clone or download this project to your local machine.

2.    Navigate to the Project Directory
Open a terminal and navigate to the project directory:

cd /path/to/project

3.    Install Required Packages
This project requires requests for making API calls and pytest for testing. Install them using pip:

pip install requests pytest

Test Scenarios

The test suite includes the following scenarios:

1.    Add a New Pet to the Store
•    Positive: Send valid data for a new pet and verify it is successfully added with status code 200.
•    Negative: Send incomplete data (e.g., without a name) to add a pet, expecting a status code 400 or 422.
2.    Update Pet Status
•    Positive: Change the status of an existing pet from “available” to “sold” and confirm the update with status code 200.
•    Negative: Attempt to change the status of a non-existent pet, expecting a 404 error.
3.    Delete a Pet
•    Positive: Delete an existing pet by ID and verify the status code is 200.
•    Negative: Try deleting a non-existent pet, expecting a 404 error.
4.    Place a New Order in the Store
•    Positive: Place an order for a pet and confirm creation with status code 200.
•    Negative: Place an order with missing data (e.g., no pet ID), expecting a 400 error.
Test Implementation

The test scenarios are implemented in Python with Pytest and Requests. Here is a sample code snippet:

import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_add_new_pet():
    pet_data = {
        "id": 12345,
        "name": "Bobby",
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Bobby"

For the full implementation, refer to the provided code in this README.

Running the Tests

1.    Run All Tests
To execute all test cases in the project, run:

pytest filename.py

Replace filename.py with the actual filename containing your test cases.

2.    Check Test Results
After running the command, Pytest will show the results for each test scenario.

Additional Notes

•    Response Schema Validation:
For more accurate testing, consider using jsonschema to validate the structure of API responses.
    •    Environment Configuration:
Environment files (e.g., .env) can be used to store and manage environment variables, such as the base URL of the API.

This README covers the setup, installation, test scenarios, and instructions to run automated tests for the Pet Store API project.
