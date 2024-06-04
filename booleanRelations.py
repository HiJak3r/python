#!/bin/python3

# Boolean Expressions are simply just a true or false statement
bool1 = True
bool2 = 3*3 == 9 # == means something is equal to something while a single = defines a variable
bool3 = False
bool4 = 3*3 != 9 # != means "does not" so 3*3 does not = 9 in our bool4 variable

print(bool1,bool2,bool3,bool4)
print(type(bool1)) # The type feature will show you what the variable is (show you bool, int, str)

bool5 = "True"
print(type(bool5))


print('\n')

#Relational Operators are simply math signs like more than, less than, equal to, or more

greater_than = 7 > 5 # This creates a boolean variable that will show true when printed
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) # This will equal True
test_and2 = (7 > 5) and (5 > 7) # This will equal False since 1 of the statements is false
test_or = (7 > 5) or (5 < 7) # This is True
test_or2 = (7 > 5) or (5 > 7) # This is also True since or only needs one statement to be true

test_not = not True # Not will just say it is the opposite of what was defined so in our case test_not would be False
