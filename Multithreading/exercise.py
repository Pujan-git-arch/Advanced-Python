# Create any multithreaded code using for loop for creating multithreads for i in range(10): th = Thread(target=func_name, args=(i, )) print total active threads in multithreaded code using threading.active_count()

import threading
from threading import Thread # this is the import statement that imports the Thread class from the threading module. The Thread class is used to create and manage threads in Python. It provides methods for starting, stopping, and managing threads, as well as for synchronizing access to shared resources between threads.
import time

def func_name(num):
    print(f"Thread {num} is starting")
    time.sleep(2) # this is the time.sleep() function that is used to pause the execution of the thread for a specified amount of time. In this case, the thread will sleep for 2 seconds before continuing to execute the rest of the code in the func_name function.
    print(f"Thread {num} is finishing")
    
threads = [] # this is the list that will hold all the threads that are created in the for loop. The threads will be added to this list so that we can keep track of them and wait for them to finish before moving on to the next line of code.
for i in range(10):
    th = Thread(target=func_name, args=(i,)) # this is the line of code that creates a new thread using the Thread class. The target parameter is set to the func_name function, which is the function that will be executed by the thread. The args parameter is a tuple that contains the arguments that will be passed to the func_name function when it is called by the thread. In this case, we are passing the value of i as an argument to the func_name function.
    threads.append(th)
    th.start()

print(f"Total active threads: {threading.active_count()}")

for th in threads:
    th.join() # this is the line of code that waits for the thread to finish before moving on to the next line of code. The join() method is called on the thread object, which will block the execution of the main thread until the thread has finished executing. This is important because we want to make sure that all threads have finished before we move on to the next line of code.
    
print("All threads have finished executing")
print(f"Total active threads: {threading.active_count()}") # this is the line of code that prints the total number of active threads after all threads have finished executing. The threading.active_count() function is called to get the current number of active threads in the program.