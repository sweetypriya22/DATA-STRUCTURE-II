'''
Group Words by Length

You are designing a vocabulary training module for a language learning platform. 
Users input a list of words, and the system must group them by word length while preserving their original order.
This supports level-based exercises—shorter words for beginners and longer ones for advanced learners.

To implement this feature, you are required to write a Python function named group_words_by_length(words)
that takes a list of words as input. 
The function should return a dictionary where the keys are the word lengths, 
and the values are lists containing all the words of that length. 
The relative order of words within each group must match their order of appearance in the original list. 
If the input list is empty, the function should return an empty dictionary.
'''
# Import literal_eval library to safely evaluate string input as a Python literal 
from ast import literal_eval
 
# Taking the input
words = literal_eval(input())
 
def group_words_by_length(words):
   # Write your code here
   result = {}
   for i in words:
      length = len(i)
      if length not in result:
         result[length] = []
      result[length].append(i)
   return result
      


# Print the output 
print(group_words_by_length(words))