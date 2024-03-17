from django.test import TestCase, RequestFactory
from utils.pre_processing_data.open_hours import preprocess_open_hours
from utils.pre_processing_data.food_items import preprocess_food_items
from utils.import_csv_to_mongodb import check_coordinates
from food_trucks.models import FoodTruck
from food_trucks.views import details

class PreprocessOpenHoursTestCase(TestCase):
    def test_valid_input(self):
        open_hours_str = "Mo-Fr:10AM-18AM;Sa:12AM-16AM"
        expected_output = {
            "Monday": [{"start_time": "10AM", "end_time": "18AM"}],
            "Tuesday": [{"start_time": "10AM", "end_time": "18AM"}],
            "Wednesday": [{"start_time": "10AM", "end_time": "18AM"}],
            "Thursday": [{"start_time": "10AM", "end_time": "18AM"}],
            "Friday": [{"start_time": "10AM", "end_time": "18AM"}],
            "Saturday": [{"start_time": "12AM", "end_time": "16AM"}]
        }
        self.assertEqual(preprocess_open_hours(open_hours_str), expected_output)

    def test_invalid_input(self):
        open_hours_str = "Invalid Format"
        # The function should return an empty dictionary for invalid input
        self.assertEqual(preprocess_open_hours(open_hours_str), {})

    def test_missing_hours(self):
        open_hours_str = "Mo-Fr:2AM-5AM;Sa"
        # The function should ignore the day without hours and return a dictionary for the rest
        expected_output = {
            "Monday": [{"start_time": "2AM", "end_time": "5AM"}],
            "Tuesday": [{"start_time": "2AM", "end_time": "5AM"}],
            "Wednesday": [{"start_time": "2AM", "end_time": "5AM"}],
            "Thursday": [{"start_time": "2AM", "end_time": "5AM"}],
            "Friday": [{"start_time": "2AM", "end_time": "5AM"}]
        }
        self.assertEqual(preprocess_open_hours(open_hours_str), expected_output)


class PreprocessFoodItemsTestCase(TestCase):
    def test_valid_input(self):
        food_items_data = "Pizza:Burrito:Taco"
        expected_output = ["Pizza", "Burrito", "Taco"]
        self.assertEqual(preprocess_food_items(food_items_data), expected_output)

    def test_empty_input(self):
        food_items_data = ""
        # The function should return an empty list for empty input
        self.assertEqual(preprocess_food_items(food_items_data), [])

    def test_edge_cases(self):
        food_items_data = "Pizza"
        # The function should handle single food item
        self.assertEqual(preprocess_food_items(food_items_data), ["Pizza"])

        food_items_data = "Pizza:"
        # The function should handle food item with a trailing colon
        self.assertEqual(preprocess_food_items(food_items_data), ["Pizza"])

        food_items_data = ":Pizza"
        # The function should handle food item with a leading colon
        self.assertEqual(preprocess_food_items(food_items_data), ["Pizza"])

class TestCheckCoordinates(TestCase):
    def test_valid_coordinates(self):
        # Test with valid latitude and longitude values
        self.assertTrue(check_coordinates(37.7749, -122.4194))
        self.assertTrue(check_coordinates(90, 180))
        self.assertTrue(check_coordinates(-90, -180))

    def test_invalid_coordinates(self):
        # Test with invalid latitude and longitude values
        self.assertFalse(check_coordinates(91, 0))  # Latitude exceeds the valid range
        self.assertFalse(check_coordinates(0, 181))  # Longitude exceeds the valid range
        self.assertFalse(check_coordinates(0, -181))  # Longitude exceeds the valid range
        self.assertFalse(check_coordinates(0, 0)) # We don't want value like this


class FoodTruckModelTestCase(TestCase):
    def setUp(self):
        # Create a sample FoodTruck instance for testing
        self.food_truck_data = {
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
        self.food_truck = FoodTruck(**self.food_truck_data)

    def tearDown(self):
        # Delete the FoodTruck instance after the test
        self.food_truck.delete()

    def test_food_truck_creation(self):
        # Test creating a FoodTruck instance
        self.assertEqual(self.food_truck.name, 'Test Food Truck1')
        self.assertEqual(self.food_truck.facility_type, 'Food Truck1')
        self.assertEqual(self.food_truck.location_description, 'Nearby1')
        self.assertEqual(self.food_truck.address, '1234 Test St')
        
    def test_food_truck_save_and_retrieve(self):
        # Save the FoodTruck instance to the database
        self.food_truck.save()

        # Retrieve the FoodTruck instance from the database
        retrieved_food_truck = FoodTruck.objects.get(name='Test Food Truck1')

        # Verify the retrieved data
        self.assertEqual(retrieved_food_truck.name, 'Test Food Truck1')
        self.assertEqual(retrieved_food_truck.facility_type, 'Food Truck1')
        self.assertEqual(retrieved_food_truck.location_description, 'Nearby1')
        self.assertEqual(retrieved_food_truck.address, '1234 Test St')



class DetailsViewTestCase(TestCase):
    def setUp(self):
        # Create a sample FoodTruck instance for testing
        self.food_truck_data = {
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
        self.food_truck = FoodTruck.objects.create(**self.food_truck_data)

    def tearDown(self):
        # Delete the FoodTruck instance after the test
        self.food_truck.delete()

    def test_details_view(self):
        # Create a request instance
        request = RequestFactory().get('/details/' + str(self.food_truck.id))

        # Call the details view function with the request
        response = details(request, str(self.food_truck.id))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the food truck's name
        self.assertContains(response, self.food_truck.name)



