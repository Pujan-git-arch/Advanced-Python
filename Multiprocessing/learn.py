import time
import multiprocessing

from sympy import python

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")
    
    # all the things to keep in mind in this code are as follows:
    # 1. The multiprocessing module is imported to create and manage processes in Python.
    # 2. The calc_square function is defined to calculate the square of each number in the input list and print the result.
    # 3. The calc_cube function is defined to calculate the cube of each number in the input list and print the result.
    # 4. The if __name__ == "__main__": block is used to ensure that the code inside it is only executed when the script is run directly, and not when it is imported as a module.
    # 5. The arr list is defined with the numbers [2, 3, 8] to be processed by the calc_square and calc_cube functions.
    # 6. Two Process objects, p1 and p2, are created using the multiprocessing.Process class, with the target functions set to calc_square and calc_cube, respectively, and the arr list passed as an argument to each function.
    # 7. The start() method is called on both p1 and p2 to start the processes and execute the target functions in parallel.
    # 8. The join() method is called on both p1 and p2 to wait for the processes to complete before moving on to the next line of code.     
    # 9. Finally, the message "Done!" is printed to indicate that both processes have completed their execution.
    

