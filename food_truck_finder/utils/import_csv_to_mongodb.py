import csv
from utils.pre_processing_data.open_hours import preprocess_open_hours
from utils.pre_processing_data.food_items import preprocess_food_items
from food_trucks.models import FoodTruck

def check_coordinates(lat, long):
    return lat != 0 and long != 0 and -180 <= long <= 180 and -90 <= lat <= 90

def import_csv_to_mongodb(csv_file_path):
    # Delete the data from the Database to populate it again
    documents = FoodTruck.objects
    for doc in documents:
        doc.delete()
    
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            latitude = float(row["Latitude"])
            longitude = float(row["Longitude"])

            # Check if coordinates are correct
            if not check_coordinates(latitude, longitude):
                continue

            open_hours_data = row['dayshours']
            food_items_data = row['FoodItems']
            
            open_hours_dict = dict()
            if open_hours_data:
                # preprocess the availability days and hours
                open_hours_dict = preprocess_open_hours(open_hours_data)
            
            food_items_list = []
            if food_items_data:
                #preprocess the food items into a list
                food_items_list = preprocess_food_items(food_items_data)
            
            location_data = [longitude, latitude]
            
            food_truck_object = FoodTruck(
                name = row["Applicant"],
                facility_type = row["FacilityType"],
                location_description = row["LocationDescription"],
                address = row["Address"],
                permit = row["permit"], 
                status = row["Status"],
                food_items = food_items_list,
                location = location_data,
                open_hours = open_hours_dict
            )

            food_truck_object.save()

