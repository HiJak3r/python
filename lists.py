#!/bin/python3

# Lists have brackets []
movies = ["Indiana Jones", "Men in Black", "Godzilla", "Night at the Museum"]

# Be mindful that computers all start from 0 when working with numbers
# Our list in order goes [0,1,2,3]
# To call data from a list, use what is called an index [1]
print(movies[1])
print(movies[0])
print(movies[1:3] # Will return items 1 to 3 - WILL NOT INCLUDE THE LAST INDEX

# To print from 1 all the way to the end
print(movies[1:])

# You can also do the opposite to only print up until that point
print(movies[:1])

# If you want to print the last item, you can
print(movies[-1])


# You can also apply methods to a list
print(len(movies)) # will print number of items in the list

movies.append("Star Wars") # You can append to the end of your list
print(movies)

movies.insert(2, "The Mummy") # You can also insert to a specific spot in your list
print(movies) # Here you can see The Mummy in slot 2 now


movies.pop() # removes the last item from the list
print(movies)

movies.pop(0) # removes based on index - Indiana Jones here...
print(movies)

sarah_movies = ['Just Go With It', '50 First Dates']

#You can also combine lists
our_favorite_movies = movies + sarah_movies # you don't need to store in a variable first but it's better practice
print(our_favorite_movies)


# You can also have a list within a list
grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1] # This will allow you to pull certain things within your lists - Here it would pull index Bob's grade so 0 for ["Bob", 82] and 1 for 82
print(bobs_grade)

# You can also change within the multi-list too
grades[0][1] = 83
print(grades) # You will see Bob's grade has changed
