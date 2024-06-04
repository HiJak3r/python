#!/bin/python3

# This is how you first define a function
# Indentation is EXTREMELY important in Python - the variables included in this function all are indented with a tab
def who_am_i(): # note - this is a function without parameters
	name = "Jacob" # this is a local variable - this variable is only available within this function
	age = 24
	print("My name is " + name + " and I am " + str(age) + " years old.")

# This is how you perform a call to a defined function
who_am_i()

# This is how you define a function with a parameter - A parameter is basically just another argument that is needed to use the function. In this case num
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(50)

# You can also add multiple parameters
def add(x,y):
	print(x + y)

# Each additional number is specified for the parameters needed for the function
add(7,7)

# This function will allow you to just have a piece of data that you can use further in your script
def multiply(x,y):
	return x * y # return will only return and not print to the screen - This is useful for if you wanted to use the function in another variable that needed some input or something

multiply(7,7) # This won't print anything since there isn't a print in the function
print(multiply(7,7)) # To print you will need to do something like this or add the print statement to the function


# Functions also allow you to use the local variable just like you would with normal math functions
def square_root(x):
	print(x ** .5)

square_root(64)


# To make things simple, you can use something like this to just make a new line if you are going to be using it often
def nl():
	print('\n')

nl()
