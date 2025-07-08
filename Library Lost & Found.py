'''
Library Lost & Found
The local library runs a "Lost and Found" system to manage misplaced books. Patrons report books as lost using their ISBNs, and the library staff scans ISBNs of books found in the overnight bin.

Your task is to help automate three important checks:
Reunification Check: Identify which ISBNs were both, 
reported lost and later found — these can be returned to their rightful owners
Ghost Scan Check: Identify ISBNs that were found but were never reported lost — these are likely ghost scans or misfiled books
Lost Reports Count: Maintain a log of how many times each ISBN was reported lost (some books might be reported multiple times)
To implement this, write a Python function named process_lost_and_found(lost_reports, found_scans) that accepts two lists:
lost_reports: List of ISBNs reported lost; ISBNs may repeat
found_scans: List of ISBNs scanned as found; all values are unique
The function should return:

A sorted (ascending) list of ISBNs that are both in lost_reports and found_scans
A sorted (ascending) list of ghost ISBNs that are found but not in lost_reports
A dictionary mapping each ISBN in lost_reports to the number of times it was reported
'''
import ast
from collections import Counter
# Taking the inputs
lost_reports = ast.literal_eval(input())
found_scans = ast.literal_eval(input())

def process_lost_and_found(lost_reports, found_scans):
    # Write your code here
    lost_count = Counter(lost_reports)
    reunite = []
    ghost_scan = []

    for isbn in found_scans:
        if isbn in lost_reports:
            reunite.append(isbn)
        else:
            ghost_scan.append(isbn)
    return [reunite, ghost_scan, dict(lost_count)]
# Print the output
print(process_lost_and_found(lost_reports, found_scans))