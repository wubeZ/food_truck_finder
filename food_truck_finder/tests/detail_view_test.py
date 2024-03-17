import pytest

from food_trucks.models import FoodTruck
from food_trucks.views import details

# Import RequestFactory to create request instances
from django.test import RequestFactory

# Define a fixture to create and clean up the FoodTruck instance
@pytest.fixture(scope="function")
def food_truck_instance():
    # Create a sample FoodTruck instance for testing
    food_truck_data = {
        'name': 'Test Food Truck',
        'facility_type': 'Food Truck',
        'location_description': 'Nearby',
        'address': '123 Test St',
        'permit': '12345',
        'status': 'APPROVED',
        'food_items': ['Pizza', 'Burger'],
        'location': [40.7128, -74.0060],
        'open_hours': {'Monday': [{'start_time': '10:00AM', 'end_time': '18:00AM'}]}
    }
    food_truck = FoodTruck.objects.create(**food_truck_data)

    yield food_truck

    # Clean up: delete the FoodTruck instance after each test
    food_truck.delete()

# Test function with the fixture injected
def test_details_view(food_truck_instance):
    # Create a request instance
    request = RequestFactory().get('/details/' + str(food_truck_instance.id))

    # Call the details view function with the request
    response = details(request, str(food_truck_instance.id))

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the food truck's name
    assert food_truck_instance.name.encode() in response.content
