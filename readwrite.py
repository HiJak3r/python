#!/bin/python3

months = open('.\materials\months.txt')

print(months.readlines()) # months.readline() would allow you to read a line one by one

# To read lines again you must use what's called the seek method
months.seek(0)
print(months.readlines())

# You could also iterate over it using a for loop
for month in months:
	print(month.strip())

months.close()




# You can also write to a file

days = open('days.txt', "w")

days.write("Monday")

# This would overwrite the file
days.write("\nTuesday")

days.close()


# To append to a file, you need to change from write mode to append mode
days = open('days.txt', "a")

days.writes("\nWednesday")

days.close()
