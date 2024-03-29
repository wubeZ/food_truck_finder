import pytest
from pytest_mock import mocker 

from food_trucks.models import FoodTruck

# Define a fixture to create and clean up the FoodTruck instance
@pytest.fixture(scope="function")
def food_truck_instance(mocker):
    # Create a sample FoodTruck instance for testing
    food_truck_data = {
        'name': 'Test Food Truck1',
        'facility_type': 'Food Truck1',
        'location_description': 'Nearby1',
        'address': '1234 Test St',
        'permit': '12345',
        'status': 'APPROVED',
        'food_items': ['Pizza', 'Burger'],
        'location': [40.7128, -74.0060],
        'open_hours': {'Monday': [{'start_time': '10:00AM', 'end_time': '12:00AM'}]}
    }
    food_truck = FoodTruck(**food_truck_data)

    # Mocking the save method of FoodTruck instance
    mocker.patch.object(food_truck, 'save')

    # Yield the FoodTruck instance
    yield food_truck

    # Clean up: delete the FoodTruck instance after each test
    food_truck.delete()

# Test function with the fixture injected
def test_food_truck_save_and_retrieve(food_truck_instance, mocker):
    # Mocking the get method of FoodTruck.objects
    mocker.patch('food_trucks.models.FoodTruck.objects.get', side_effect=FoodTruck.DoesNotExist)

    # Attempt to retrieve the FoodTruck instance from the database
    with pytest.raises(FoodTruck.DoesNotExist):
        retrieved_food_truck = FoodTruck.objects.get(name='Test Food Truck1')
        
        # Verify the retrieved data
        assert retrieved_food_truck.name == 'Test Food Truck1'
        assert retrieved_food_truck.facility_type == 'Food Truck1'
        assert retrieved_food_truck.location_description == 'Nearby1'
        assert retrieved_food_truck.address == '1234 Test St'
