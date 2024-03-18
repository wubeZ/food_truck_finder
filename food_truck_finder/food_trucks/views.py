from django.shortcuts import render
from food_trucks.models import FoodTruck
from bson import ObjectId

def nearest_trucks(lat, lng):
    # Convert latitude and longitude to float
    lat = float(lat)
    lng = float(lng)

    # Perform aggregation pipeline to calculate distance and find the 6 closest trucks
    pipeline = [
        {
            "$geoNear": {
                "near": {"type": "Point", "coordinates": [lng, lat]},
                "distanceField": "distance_miles",
                "spherical": True,
                "distanceMultiplier": 0.000621371,  # Convert meters to miles
                "query": {}
            }
        },
        {
            "$match" : {"status": "APPROVED"}
        },
        {
            "$sort": {"distance_miles": 1}  # Sort by distance in ascending order
        },
        {
            "$project": {
                "_id": 0,
                "id": "$_id",
                "name": 1,
                "facility_type": 1,
                "location_description": 1,
                "address": 1,
                "permit": 1,
                "status": 1,
                "food_items": 1,
                "location": 1,
                "open_hours": 1,
                "distance_miles": 1
            }
        },{
            "$limit": 6 # Limit to 6 results
        }
    ]

    # Execute the aggregation pipeline
    nearest_trucks = list(FoodTruck.objects.aggregate(*pipeline))

    return nearest_trucks


def index(request):
    context = {
        'variable': 'value',
    }
    return render(request, 'home.html', context)


def search(request):
    context = {}
    if request.method == 'GET':
        truck_name = request.GET.get('search')

        food_trucks = FoodTruck.objects(name=truck_name)

        context = {
            "food_trucks": food_trucks
        }
    return render(request, "search_by_location.html", context)

def search_by_location(request):
    context = {}
    if request.method == 'GET':
        # Process the received coordinates
        lat = request.GET.get('latitude')
        lng = request.GET.get('longitude')

        food_trucks = nearest_trucks(lat, lng)

        context = {
            "food_trucks" : food_trucks
        }

    return render(request, "search_by_location.html", context)

def details(request, id):
    object_id = ObjectId(id)
    
    food_truck = FoodTruck.objects.get(id=object_id)
    
    context = {
        "food_truck" : food_truck
    }
    return render(request, "details.html", context)

