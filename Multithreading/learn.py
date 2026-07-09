import time
import threading


def calc_Square(numbers):
    print("Calculate the square of numbers in the list")
    for n in numbers:
        time.sleep(0.2)
        print( "square: ", n * n)
        
def calc_Cube(numbers):
    print("Calculate the cube of numbers in the list")
    for n in numbers:
        time.sleep(0.2)
        print( "cube: ", n * n * n)
        
arr= [2,3,8,9]

t = time.time() # to calculate the total time taken by the program # this is the starting time of the program
t1 = threading.Thread(target=calc_Square, args=(arr,)) # this is the thread that will run the calc_Square function with the arr list as an argument #args is a tuple that contains the arguments to be passed to the function only one argument is passed to the function so we need to put a comma after the argument to make it a tuple
t2 = threading.Thread(target=calc_Cube, args=(arr,))    
t1.start() # here we are starting the thread t1 which will run the calc_Square function in a separate thread
t2.start()
t1.join() # here we are waiting for the thread t1 to finish before moving on to the next line of code. This is important because we want to make sure that the calc_Square function has finished before we move on to the next line of code. If we don't do this, the program will continue to run and will not wait for the calc_Square function to finish. This can cause problems because the calc_Square function may not have finished before the program moves on to the next line of code.
t2.join()
print("Total time taken: ", time.time() - t) # here we are calculating the total time taken by the program by subtracting the starting time from the current time. This will give us the total time taken by the program in seconds.
print("Done!")

# the flow of program is as follows:
# 1. The program starts and the starting time is recorded.
# 2. Two threads are created, one for calculating the square of the numbers in the list and one for calculating the cube of the numbers in the list.
# 3. The threads are started and the program waits for them to finish.  
# 4. Once the threads have finished, the total time taken by the program is calculated and printed.

# the flow of the thread and calc square and calc cube functions is as follows:
# 1. The calc_Square function is called and the square of each number in the list is calculated and printed.
# 2. The calc_Cube function is called and the cube of each number in the list is calculated and printed.    
# 3. The program waits for both threads to finish before moving on to the next line of code.