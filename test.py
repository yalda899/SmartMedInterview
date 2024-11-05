import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

#add a new pet
def test_add_new_pet():
    pet_data = {
        "id": 12345,
        "name": "Bobby",
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Bobby"

def test_add_new_pet_with_missing_data():
    pet_data = {
        "id": 12345,
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 400 or response.status_code == 422

# update pet status
def test_update_pet_status():
    pet_data = {
        "id": 12345,
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    assert response.json()["status"] == "sold"

def test_update_non_existent_pet():
    pet_data = {
        "id": 99999,
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 404

#delete pet
def test_delete_pet():
    pet_id = 12345
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200

def test_delete_non_existent_pet():
    pet_id = 99999
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 404

#place an order
def test_place_order():
    order_data = {
        "id": 54321,
        "petId": 12345,
        "quantity": 1,
        "status": "placed"
    }
    response = requests.post(f"{BASE_URL}/store/order", json=order_data)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"

def test_place_order_with_missing_data():
    order_data = {
        "id": 54321,
        "quantity": 1,
        "status": "placed"
    }
    response = requests.post(f"{BASE_URL}/store/order", json=order_data)
    assert response.status_code == 400