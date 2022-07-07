import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 2000000000
SLEEP = 10

def io_bound(sec):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(F"{pid} * {processName} * {threadName} \ -----> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} \ ---->Finished sleeping...")

def cpu_bound(n):

    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} \  ------>Start counting....")
    while n>0:
        n -= 1

    print(f"{pid} * {processName} * {threadName} \ ---> Fininshed counting...")

if __name__ == "__main__":
    start = time.time()
    io_bound(10)
    io_bound(5)
    end = time.time()
    print("start time", start)
    print("end time", end) 
    print('Time taken in seconds -', end - start)
    print('date tiem', time.asctime(time.localtime(end-start)))