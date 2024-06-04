#!/bin/python3

my_name = "Jacob"
print(my_name[0]) # will print first letter of my_name
print(my_name[-1]) # will print last letter of my_name

# Strings are not mutable but you can change the value of a string instead

sentence = "This is a sentence."
print(sentence[:4]) # This would allow you to grab the 4th indexed word
print(sentence.split()) # This is known as a delimiter which will split up the string - the default character to split by is a space

# You can both split and join strings
# This will split the sentence string to ['This', 'is', 'a', 'sentence.']
sentence_split = sentence.split()

# This will join our strings together after our split and put a space between each string
sentence_join = ' '.join(sentence_split)
print(sentense_join)

# You can use the ' or " interchangably within a string to form one
quote = "He said, 'give me all your money'"
print(quote)

# You can also use character escaping too by addind a \ in front of each one you want to escape
quote = "He said, \"give me all your money\""
print(quote)

too__much_space = "                     hello        "
print(too_much_space.strip()) # This will remove any unnecessary characters/spaces

#This will allow you to get a boolean and check if a letter is in a string
print("A" in "Apple") # This will return a True boolean
print("a" in "Apple") # This will return a False boolean

# If you want to check for both upper and lowercase in the string, you could do this
letter = "A"
word = "Apple"
print(letter.lowerr() in word.lower())

# You can use the string format method to add strings to strings
movie = "Men in Black"
print("My favorite movie is {}.".format(movie))

# This is called percent format
print("My favorite movie is %s." % movie)

# You could also use a literal or f string
print(f"My favorite movie is {movie}.")
