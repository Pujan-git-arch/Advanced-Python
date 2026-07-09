import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time= time.time()
        print(f"Execution time: {(end_time - start_time)*1000} milliseconds")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

array = range(1,100000)
cout_square = calc_square(array)
cout_cube = calc_cube(array)