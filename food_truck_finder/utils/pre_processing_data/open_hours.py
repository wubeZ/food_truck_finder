from collections import defaultdict

def preprocess_open_hours(open_hours_str):
    # Define a dictionary to map abbreviated days to the index number in day_mapping array
    day_number = {
        "Su": 6, "Mo": 0, "Tu": 1, "We": 2, "Th": 3, "Fr": 4, "Sa": 5
    }
    
    day_mapping = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    # Use defaultdict to automatically create lists for each day
    processed_open_hours = defaultdict(list)  
    
    days_hours_pairs = open_hours_str.split(';')
    
    for pair in days_hours_pairs:
        parts = pair.split(':')
        if len(parts) == 2:  # Ensure that the pair contains both day range and hours
            day_range, hours = parts[0], parts[1]
            if day_range.find('/') != -1:  # Check if day range contains multiple days separated by '/'
                days = day_range.split('/')
                
            elif day_range.find('-') != -1: # Check if day range contains multiple days separated by '-'
                start_day, end_day = day_range.split('-')
                start_index = day_number.get(start_day, -1)
                end_index = day_number.get(end_day, -1)
                if start_index != -1 and end_index != -1:
                    days = []
                    for i in range(start_index, end_index + 1):
                        days.append(day_mapping[i])
                else:
                    days = [day_range]
            else:
                days = [day_range]
            
            # Split the hours into different time slots
            time_slots = hours.split('/')
            
            for day in days:
                index = day_number.get(day, -1)
                if index == -1:
                    full_day = day
                else:
                    full_day = day_mapping[index] # Get the full day name from the array
                for time_slot in time_slots:
                    start_time, end_time = time_slot.split('-')
                    processed_open_hours[full_day].append({"start_time": start_time, "end_time": end_time})
        else:
            # Handle invalid format or missing day/hours
            print(f"Ignoring invalid format: {pair}")
    
    return dict(processed_open_hours)