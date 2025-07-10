'''
You need to create a feature for an application that counts how many times each character appears in user text, ignoring case. This will help identify frequently used characters or assist in building predictive models at the character level.
To implement this, you are required to create a Python function named count_characters(s) that accepts a single string as input and returns a dictionary. The keys of this dictionary should be lowercase characters, and the values should be the number of times each character appears in the input string. The character count must be case-insensitive, i.e., both uppercase and lowercase versions of a character must be treated as the same and stored as a lowercase key.
The function must:
Treat uppercase and lowercase letters as the same (i.e., case-insensitive counting)
Accept only valid input consisting of non-empty alphabetic characters
Return appropriate error messages for invalid inputs, such as strings containing non-alphabetic characters

Input format
A single line containing the string s
To be considered valid, the string must be non-empty and contain only alphabetic characters (letters A–Z or a–z)

Output format
If the input string is valid, output a dictionary with lowercase characters as keys and their frequency as values
If the input contains any non-alphabetic characters (digits, symbols, whitespace, etc.), output the message: Input must contain only alphabetic characters.

Constraints
The input string cannot be empty

'''

# Taking the input
s = input()

def count_characters(s):
    # Write your code here
    if not isinstance(s, str) or not s.isalpha():
        return "Input must contain only alphabetic characters."
    s = s.lower()
    Set = {}
    for i in s:
        Set[i] = Set.get(i, 0) + 1

    return Set
# Print the output
print(count_characters(s))