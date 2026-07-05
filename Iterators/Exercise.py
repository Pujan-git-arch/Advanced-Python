# Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
# The iterator should stop when it reaches a limit defined in the constructor.
# Solution

class Fibonacci:
    def __init__(self, limit):
        # default constructor
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration


# init the fib_iterator
fib_iterator = iter(Fibonacci(5)) # Create an instance of the Fibonacci iterator with a limit of 5 .. why no instance of Fibonacci is created here? because we are creating an instance of the iterator and not the class itself. The iterator is created by calling the iter() function on the Fibonacci class, which returns an iterator object that can be used to iterate over the Fibonacci series.
while True:
    # print the value of next fibonacci up to 5th fibonacci
    try:
        print(next(fib_iterator))
    except StopIteration:
        break