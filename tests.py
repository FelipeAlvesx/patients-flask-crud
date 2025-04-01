import requests
import pytest


BASE_URL = 'http://127.0.0.1:5000'
patients = []

def test_add_patient():
    new_patient_data = {
        "name": "Pablo Gaviria Escobar",
        "age": "56",
        "description": "Knifed",
        "room": "42"
    }
    response = requests.post(f"{BASE_URL}/add-patient", json=new_patient_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    patients.append(response_json['id'])

def test_get_patients():
    response = requests.get(f"{BASE_URL}/patients")
    assert response.status_code == 200
    response_json = response.json()
    assert "patients" in response_json
    assert "total_patients" in response_json

def test_get_patient():
    if patients:
        patient_id = patients[0]
        print(patients)
        response = requests.get(f"{BASE_URL}/patients/{patient_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert patient_id == response_json['id']
    
def test_update_patients():
    if patients:
        patient_id = patients[0]
        payload = {
        "name": "Pablo Gaviria Escobar",
        "age": "56",
        "description": "Knifed, in stomach",
        "room": "42",
        "discharge": True
    }
        response = requests.put(f"{BASE_URL}/patients/{patient_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json
        assert patient_id == response_json['id']
        
        response = requests.get(f"{BASE_URL}/patients/{patient_id}")
        assert response.status_code == 200
        response_json = response.json()
        for key in payload: 
            assert response_json[key] == payload[key]
            
def test_delete_patient():
    if patients:
        patient_id = patients[0]
        response = requests.delete(f"{BASE_URL}/patients/{patient_id}")
        assert response.status_code == 200
        
        response = requests.get(f"{BASE_URL}/patients/{patient_id}")
        assert response.status_code == 404
            


        