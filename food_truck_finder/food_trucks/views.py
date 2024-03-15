from django.shortcuts import render
from food_trucks.models import FoodTruck

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
            "$sort": {"distance_miles": 1}  # Sort by distance in ascending order
        },
        {
            "$project": {
                "_id": 0,
                "name": 1,
                "facility_type": 1,
                "location_description": 1,
                "address": 1,
                "permit": 1,
                "status": 1,
                "food_items": 1,
                "latitude": 1,
                "longitude": 1,
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


def my_view(request):
    context = {
        'variable': 'value',
    }
    
    return render(request, 'base.html', context)