#!/bin/python

# To accept user input, you just need to use the input function
name = input("Enter your name: ")
drink = input("What's your favorite drink?: ")
print("Hello " + name + "!" + "Have a " +drink+ ".")

print("\n")

x = float(input("Give me a number: "))
y = float(input("Anotha one: "))
o = input("Give me an operator: ")

if o == "+"
	print(x + y)
elif o == "-"
	print(x - y)
elif o == "*"
	print(x * y)
elif o == "/"
	print(x / y)
elif o == "**"
	print(x ** y)
else
	print("ERROR: Unknown operator")
	print("SYNTAX: \"+\" for addition or \"-\" for subtraction or \"*\" for multiply or \"/\" for division or \"**\" for exponents")
