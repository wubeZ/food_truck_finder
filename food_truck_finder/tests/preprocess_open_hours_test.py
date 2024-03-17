import pytest

from utils.pre_processing_data.open_hours import preprocess_open_hours


def test_valid_input():
    open_hours_str = "Mo-Fr:10AM-18AM;Sa:12AM-16AM"
    expected_output = {
        "Monday": [{"start_time": "10AM", "end_time": "18AM"}],
        "Tuesday": [{"start_time": "10AM", "end_time": "18AM"}],
        "Wednesday": [{"start_time": "10AM", "end_time": "18AM"}],
        "Thursday": [{"start_time": "10AM", "end_time": "18AM"}],
        "Friday": [{"start_time": "10AM", "end_time": "18AM"}],
        "Saturday": [{"start_time": "12AM", "end_time": "16AM"}]
    }
    assert preprocess_open_hours(open_hours_str) == expected_output

def test_invalid_input():
    open_hours_str = "Invalid Format"
    # The function should return an empty dictionary for invalid input
    assert preprocess_open_hours(open_hours_str) == {}

def test_missing_hours():
    open_hours_str = "Mo-Fr:2AM-5AM;Sa"
    # The function should ignore the day without hours and return a dictionary for the rest
    expected_output = {
        "Monday": [{"start_time": "2AM", "end_time": "5AM"}],
        "Tuesday": [{"start_time": "2AM", "end_time": "5AM"}],
        "Wednesday": [{"start_time": "2AM", "end_time": "5AM"}],
        "Thursday": [{"start_time": "2AM", "end_time": "5AM"}],
        "Friday": [{"start_time": "2AM", "end_time": "5AM"}]
    }
    assert preprocess_open_hours(open_hours_str) == expected_output
