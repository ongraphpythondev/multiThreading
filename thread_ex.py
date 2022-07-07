import threading
import time 

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.ThreadID = threadID
        self.name = name
        self.counter = counter 
    
    def run(self):
        print("Starting "+ self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting"+ self.name)

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 3)
thread2 = myThread(2, "Thread-2", 10)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting main thread")