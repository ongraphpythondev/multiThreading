import multiprocessing
import os 
import time 

def print_cube(num):
    count = 100000000
    print("Cube:{}".format(num*num*num))
    print(f"process-id ----> {os.getpid()} ")
    while True:
        if count == 0:
            break
        count -= 1

def print_square(num):
    count = 100000000
    print("Square:{}".format(num*num))
    print(f"process-id ----> {os.getpid()}")
    while True:
        if count == 0:
            break
        count -= 1

if __name__ == "__main__":
    p1=multiprocessing.Process(target=print_square, args=(10,))
    p2=multiprocessing.Process(target=print_cube, args=(10,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()