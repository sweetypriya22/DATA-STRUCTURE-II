'''
Swap Keys and Values in a Dictionary

You are developing a utility function for a configuration processing tool that works with key-value maps. One of the features required is the ability to reverse a mapping — that is, for each key-value pair, the value becomes the new key, and the key becomes the new value. This functionality is useful for quick lookups in reverse, such as finding configuration names based on their assigned values.



To implement this, you are required to write a Python function named swap_keys_and_values(data) that accepts a dictionary with keys and unique, hashable values. The function should return a new dictionary in which all original key-value pairs are swapped — each original value becomes a key, and each original key becomes the corresponding value.

'''

# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
data = literal_eval(input())
result = {}
def swap_keys_and_values(d):
    # Write your code here
    result = { ch:i for i,ch in d.items()}
    return result



# Print the output
print(swap_keys_and_values(data))