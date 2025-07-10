'''
Global Conference Attendees
An international conference that runs for three days stores daily records of attendees grouped by their country codes. Each day's data is represented as a dictionary where:
Each key is a country code
Each value is a list of attendee names
Your task is to write a function analyse_attendance(daily_data) that performs the following operations:

Compute a unique sorted list of country codes that were present on every single day of the conference
Build a registry mapping each country code to a sorted list of all unique attendees from that country across all days
Identify the unique sorted list of country codes that were present on the first day but absent on the last day

Input Format
A list of dictionaries representing daily attendance records
Each dictionary must have the country code (str) as the key and a list of attendees (str) as the value

Output Format
Return a list with three elements, in order: A sorted (ascending) list of country codes (str) present every day
A dictionary mapping country codes (str) to a sorted (ascending) list of all unique attendees (str)
A sorted (ascending) list of country codes (str) present on the first day but absent on the last day
'''

# Import literal_eval library to safely evaluate string input as a Python literal 
from ast import literal_eval 

# Taking the input
daily_data = literal_eval(input())

def analyse_attendance(daily_data):
    # Write your code here
    all_days = [set(day.keys()) for day in daily_data]
    common_codes = sorted(set.intersection(*all_days))

    # Step 2: Build registry of all unique attendees per country
    registry = {}
    for day in daily_data:
        for country, names in day.items():
            if country not in registry:
                registry[country] = set()
            registry[country].update(names)
    
    # Convert sets to sorted lists
    for country in registry:
        registry[country] = sorted(registry[country])

    # Step 3: Countries present on first day but not on last day
    first_day = set(daily_data[0].keys())
    last_day = set(daily_data[-1].keys())
    missing_on_last_day = sorted(first_day - last_day)

    return [common_codes, registry, missing_on_last_day]


# Print the output
print(analyse_attendance(daily_data))