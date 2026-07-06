# Create a set which only contains unique sqaures from a given a integer list.
# integer = [1, -1, 2, -2, 3, -3]
# sq_set = {1, 4, 9}

integer = [1, -1, 2, -2, 3, -3] #the given integer list
sq_set = {i**2 for i in integer} #the set comprehension that generates the unique squares of the integers in the list
print(sq_set)