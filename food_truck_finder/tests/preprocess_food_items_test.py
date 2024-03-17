import pytest

from utils.pre_processing_data.food_items import preprocess_food_items

def test_valid_input():
    food_items_data = "Pizza:Burrito:Taco"
    expected_output = ["Pizza", "Burrito", "Taco"]
    assert preprocess_food_items(food_items_data) == expected_output

def test_empty_input():
    food_items_data = ""
    assert preprocess_food_items(food_items_data) == []

def test_edge_cases():
    food_items_data = "Pizza"
    # The function should handle single food item
    assert preprocess_food_items(food_items_data) == ["Pizza"]

    food_items_data = "Pizza:"
    # The function should handle food item with a trailing colon
    assert preprocess_food_items(food_items_data) == ["Pizza"]

    food_items_data = ":Pizza"
    # The function should handle food item with a leading colon
    assert preprocess_food_items(food_items_data) == ["Pizza"]
