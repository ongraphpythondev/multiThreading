import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    if name == 1:
        time.sleep(50)
    elif name == 2:
        time.sleep(100)
    else:
        time.sleep(150)

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x1 = threading.Thread(target=thread_function, args=(1,))
    x2 = threading.Thread(target=thread_function, args=(2,))
    x3 = threading.Thread(target=thread_function, args=(3,))
    logging.info("Main    : before running thread")
    x1.start()
    x2.start()
    x3.start()
    logging.info("Main    : wait for the thread to finish")
    # x1.join()
    # x2.join()
    logging.info("Main    : all done")