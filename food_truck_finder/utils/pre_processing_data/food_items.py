
def preprocess_food_items(food_items_data):
    results = food_items_data.split(":")
    results = [elem for elem in results if elem]
    return results