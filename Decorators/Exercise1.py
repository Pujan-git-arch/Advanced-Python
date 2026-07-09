# Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

# Create a factorial function which finds the factorial of a number.

# Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

# example: 

#     factorial(1.354) : raise Exception or print error message
#     factorial(-1) : raise Exception or print error message
#     factorial(5) : 60

def check_non_negative_integer(func):
    def wrapper(n):
        if n >=0 and isinstance(n, int):
            return func(n)
        else:
            raise TypeError("Input must be a non-negative integer")
    return wrapper

@check_non_negative_integer
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
print(factorial(1.354))  # Raises TypeError: Input must be a non-negative integer
print(factorial(-5))  # Raises TypeError: Input must be a non-negative integer
