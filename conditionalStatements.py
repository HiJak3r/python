#!/bin/python3

# Conditional statements are basically if/else statements

# This function will use an if/else statement to decide what output gets returned
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!" # Keep in mind indentation
	else:
		return "No drink for you!"

print(drink(3)) # You will get a drink
print(drink(1)) # You wont get a drink

# You can use conditional statements to add more than one option if you want to using else if (elif)
# You can even use relational operators too
def alcohol(age,money):
	if(age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money!"
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too young and too poor."

print(alcohol(21,5))
print(alcohol(32,4))
print(alcohol(20,5))
print(alcohol(20,4))
