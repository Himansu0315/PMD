# import pytest
# from app import app

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_predict_result(client):
#     # Prepare test data
#     test_data = {
#         'Type': 'L',
#         'Air_temperature_K': 300,
#         'Process_temperature_K': 400,
#         'Rotational_speed_rpm': 2000,
#         'Torque_Nm': 50,
#         'Tool_wear_min': 100
#     }

#     # Make a POST request to the predict route
#     response = client.post('/predict', json=test_data)

#     # Check if the response status code is 200
#     assert response.status_code == 200

#     # Check if the response contains the predicted target and failure
#     data = response.json
#     assert 'target_prediction' in data
#     assert 'failure_prediction' in data

#     # Check if the predictions are integers
#     assert isinstance(data['target_prediction'])
#     assert isinstance(data['failure_prediction'])

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_result(client):
    # Define your test data
    test_data = {
        "Type": "L",
        "Air_temperature_K": 300,
        "Process_temperature_K": 400,
        "Rotational_speed_rpm": 200,
        "Torque_Nm": 30,
        "Tool_wear_min": 50
    }

    # Send a POST request to your Flask route
    response = client.post('/predict', json=test_data)

    # Check if the response is valid
    assert response.status_code == 200

    # Check if the response contains the expected keys
    assert 'target_prediction' in response.json
    assert 'failure_prediction' in response.json

    # Optionally, you can check the format or type of the response values
    assert isinstance(response.json['target_prediction'], str)
    assert isinstance(response.json['failure_prediction'], str)

    # Add more assertions as needed to verify the correctness of the predictions

# You can add more test cases for other routes or functions if needed
