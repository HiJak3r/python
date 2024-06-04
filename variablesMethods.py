#!/bin/python3

# You can store a piece of data in a variable - you can name the variable anything "quote" is just a demo variable name
quote = "All is fair in love and war."
print(quote)

# You can also add what is called a method to do additional functions to your variable
# This will make each letter upper case in the print statement
print(quote.upper())

# This will make each letter lower case in the print statement
print(quote.lower())

# This will capitalize the first letter of each word in the string for our print statement
print(quote.title())

# This will allow you to print the length of the characters in the quote variable
print(len(quote))



# You can store various data sets within a string as such
name = "Jacob" # This is a string
age = 24 # This is and integer
gpa = 3.7 # This is a float (number with a decimal)

# You can use the int() method to change a string to an integer
print(int(age))

# Even if you specify a float, it will print only an integer - In this case it will print 30
print(int(30.1))

# Any time you print an integer it will always round down
print(int(30.9))

# This example is to show you that you can only concatenate strings and not integers - In order for this to work, we must make our age variable a string
print("My name is " + name + " and I am " + str(age) + " years old.")

# Since age is a variable, that means it can change - hense the name
age += 1
print(age) # This will now print my age + 1 year so 25

# We can also add with multiple variables
birthday = 1
age += birthday
print(age) # This will print 26 since the script works top to bottom
