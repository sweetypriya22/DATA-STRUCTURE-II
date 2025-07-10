'''
In a mystical kingdom, alchemists are tasked with gathering ingredients daily to brew powerful magical potions. The kingdom tracks new discoveries and checks which potions can be brewed based on the day’s collection.
You are to perform two tasks:
New Discoveries: Identify which ingredients gathered today are completely new (i.e., not previously known).
Brewable Potions: Determine which potions from the recipe book can be brewed using the ingredients collected today.
To automate this, write a Python function named evaluate_pantry(today_ingredients, known_ingredients, recipe_book) that accepts three inputs: a list of ingredients collected today, a list of ingredients obtained in the past, excluding today, and a dictionary mapping potion names to lists of required ingredients.
The function should return a list with:

A sorted (ascending) list of newly obtained ingredients, i.e., ingredients which are present in today’s collection but not in known ones
A list of potion names that can be brewed using today’s ingredients (order does not matter)

Input Format

today_ingredients: List of ingredients (str) collected today
known_ingredients: List of ingredients (str) obtained in the past, excluding today
recipe_book: A dictionary mapping potion names (str) to lists of required ingredients (str)

Output Format
A list with two elements:
A sorted (ascending) list of newly obtained ingredients (str)
A list of potion names (str) that can be brewed today
'''
from ast import literal_eval

# 📥 Taking inputs
today_ingredients = literal_eval(input())
known_ingredients = literal_eval(input())
recipe_book = literal_eval(input())

def evaluate_pantry(today_ingredients, known_ingredients, recipe_book):
    # Find newly discovered ingredients
    newly_discovered = sorted(set(today_ingredients) - set(known_ingredients))

    # 🧪 Find brewable potions (all ingredients must be present today)
    brewable = []
    today_set = set(today_ingredients)
    for potion, ingredients in recipe_book.items():
        if all(item in today_set for item in ingredients):
            brewable.append(potion)

    return [newly_discovered, brewable]

# 🎯 Function call
print(evaluate_pantry(today_ingredients, known_ingredients, recipe_book))