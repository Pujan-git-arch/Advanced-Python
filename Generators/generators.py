def fibonacci(): # this is a generator function that generates fibonacci series up to 100
    
    a,b = 0,1
    while True: # this is an infinite loop that will keep generating fibonacci numbers until we break out of it
        yield a  #yield is a keyword that is used to return a value from a generator function. It is similar to return, but it allows the function to be paused and resumed later. When the generator function is called, it returns a generator object that can be iterated over using the next() function. Each time next() is called, the function resumes execution from where it left off and continues until it reaches the next yield statement or the end of the function.
        a,b = b, a+b

for num in fibonacci():
    if num > 100:
        break
    print(num)
    
    # the flow of the programs is as follows:
    # 1. The fibonacci() function is called, which returns a generator object.
    # 2. The for loop iterates over the generator object, calling next() on it each time.
    # 3. The yield statement in the fibonacci() function pauses the function and returns the current value of a.
    # 4. The next() call in the for loop resumes the fibonacci() function and continues execution until the next yield statement is encountered.
    # 5. This process repeats until the break statement is encountered, which exits the for loop.
    
    # at first a=0, b=1, so the first value yielded is 0. 
    # then it checks while True, which is always true, so it yields the next value of a, which is 1.
    # then it checks while True, which is always true, so it yields the next value of a, which is 1.
    # then it checks while True, which is always true, so it yields the next value of a, which is 2.        
    # then it checks while True, which is always true, so it yields the next value of a, which is 3.
