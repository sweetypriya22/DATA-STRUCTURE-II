'''
Identify Unique Guest Names
You are managing guest check-ins for a high-profile party. As guests arrive, their names are logged into a list. However, due to the venue having multiple entrances, some names may appear more than once.
To ensure an accurate headcount you must identify the unique guests who attended the party.
Write a function unique_guests(guest_list) that:
Accepts a list of guest names
Returns a list of unique guest names in alphabetical order
'''
# Import literal_eval to safely evaluate the input string as a Python list
from ast import literal_eval

# Taking the input 
guest_list = literal_eval(input())

def unique_guests(guest_list):
    # Write your code here
    result = []
    for i in guest_list:
        if i not in result:
            result.append(i)
            result.sort()
    return result


# Print the output
print(unique_guests(guest_list))
