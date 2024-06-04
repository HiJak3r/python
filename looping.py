#!/bin/python3

# For loops - start to finish of an iteration

# This will create a list then print out each index from the list
vegetables = ["cucumber","spinach","cabbage"]
for x in vegetables: # You can name x anything you want
	print(x)

# This would allow you to do something like ping sweep
ip = 1..254
for x in ip:
	ping 192.168.1.x


# While loops - execute as long as True

# This will iterate as long as the statement is true
i = 1
while i < 10:
	print(i)
	i += 1
