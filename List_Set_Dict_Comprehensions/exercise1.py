# Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.
# Example :

#     integer = [0, 1, 2, 3, 4]
#     binary = ["0", "1", "10", "11", "100"]
#     binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = {integer:binary for integer, binary in zip(integer, binary)} #the dictionary comprehension that generates the mapping of integers to their binary values using the zip function to pair the elements of the two lists together
print(binary_dict)