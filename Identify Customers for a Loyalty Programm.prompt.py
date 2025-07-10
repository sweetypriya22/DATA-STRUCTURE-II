'''
You are working for a retail store that wants to run a loyalty programme. The marketing team provides you with two lists:

One with customers who made purchases this month
Another with customers who subscribed to the store's newsletter


Your job is to:

Find customers eligible for the loyalty programme (those who did both)
Find potential leads (those who subscribed but did not purchase)
Find inactive customers (those who purchased but are not subscribers)


Input Format

A list of names (str) of the customers who made purchases this month
A list of names (str) of the customers who subscribed to the store's newsletter


Output Format

A dictionary with the following keys and values:
'loyalty': sorted list of customers (str) in both lists
'leads': sorted list of customers (str) in both lists
'inactive': sorted list of customers (str) in both lists

'''
# Import literal_eval to safely evaluate the input string as a Python list
from ast import literal_eval

# Taking the input 
purchased = set( literal_eval(input()))
subscribed = set(literal_eval(input()))

def analyse_customers(purchased, subscribed):
    # Write your code here
    loyalty = purchased & subscribed              # present in both
    leads = subscribed - purchased                # only subscribed
    inactive = purchased - subscribed             # only purchased

    Set = {'loyalty':sorted(list(loyalty)),'leads':sorted(list(leads)),'inactive': sorted(list(inactive))}
    
    return Set





# Print the output
print(analyse_customers(purchased, subscribed))