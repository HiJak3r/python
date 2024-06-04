#!/bin/python3

# Think of these as key/value pairs - they also use curly braces {}

# This is how you make a dictionary/key value pair list
drinks = {"White Russian": 7, "Vodka Sprite": 10, "Lemon Drop": 8} # drink is key, price is value
print(drinks)

# You can also add a list to a dictionary as well
employees = {"Finance": ["Bob","Linda","Tina"], "IT":["Gene","Louise","Teddy"], "HR":["Jimmy Jr.","Mort"]}
print(employees)

# If you missed something, you can also add to the end of the dictionary like so
employees['Legal'] = ["Mr. Frond"] # adds a new key:value pair
print(employees)

# Another way to add is like so
employees.update({"Sales": ["Andie","Ollie"]})
print(employees)

# To update a single value
drinks['White Russian'] = 8
print(drinks)

# You can also grab the value of a key with the get method
print(drinks.get("White Russian))
