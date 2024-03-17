import pytest

from utils.import_csv_to_mongodb import check_coordinates

def test_valid_coordinates():
    # Test with valid latitude and longitude values
    assert check_coordinates(37.7749, -122.4194) == True
    assert check_coordinates(90, 180) == True
    assert check_coordinates(-90, -180) == True

def test_invalid_coordinates():
    # Test with invalid latitude and longitude values
    assert check_coordinates(91, 0) == False  # Latitude exceeds the valid range
    assert check_coordinates(0, 181) == False  # Longitude exceeds the valid range
    assert check_coordinates(0, -181) == False  # Longitude exceeds the valid range
    assert check_coordinates(0, 0) == False # We don't want value like this
