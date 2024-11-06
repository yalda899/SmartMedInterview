import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

def add_new_pet(id , name , status):
    pet_data = {
        "id": id,
        "name":  name,
        "status":status
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    return response

#add a new pet
def test_TC_1():
    response = add_new_pet(id = 12345 , name= "Bobby" , status='available')
    assert response.status_code == 200
    assert response.json()["name"] == "Bobby"

def test_tc_2():
    pet_data = {
        "id": 12345,
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 400 or response.status_code == 422

# update pet status
def test_TC_3():
    pet_data = {
        "id": 12345,
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    assert response.json()["status"] == "sold"


#delete pet
def test_TC_4():
    response = add_new_pet(id=12345, name="Bobby", status='available')
    pet_id = response.json()['id']
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200

def test_TC_5():
    response = add_new_pet(id=12345, name="Bobby", status='available')
    pet_id = response.json()['id']
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 404

#place an order
def test_TC_6():
    order_data = {
        "id": 54321,
        "petId": 12345,
        "quantity": 1,
        "status": "placed"
    }
    response = requests.post(f"{BASE_URL}/store/order", json=order_data)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"

