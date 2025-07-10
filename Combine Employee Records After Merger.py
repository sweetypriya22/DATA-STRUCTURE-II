'''
Two companies, AlphaTech and BetaSoft, have recently merged. Each company maintained a separate list of employee names. However, prior to the merger, a lot of employees were already enrolled in the other company. As part of the merger process, you are tasked with maintaining a list which contains only unique employee names.

You must perform a union operation to ensure no duplicate employee names are retained in the final record. The names are case-sensitive and must be preserved exactly as they are.

Write a function merged_employees(company_a, company_b) that:
Accepts two lists of employee names
Returns a sorted list containing the unique names from both companies combined

Input Format
Two lists company_a and company_b containing unique names (str) of employees
Output Format
A sorted (ascending) list containing all values with no repeats of both employee lists
'''

# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
company_a = literal_eval(input())
company_b = literal_eval(input())

def merged_employees(company_a, company_b):
    # Write your code here
    New = set(company_a) | set(company_b)
    New = list(New)
    return sorted(New)
# Print the output
print(merged_employees(company_a, company_b))