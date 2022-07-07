from threading import Timer, current_thread
from datetime import datetime
import time


def drive(car):
    print("proccess-process")
    print(f'{datetime.now()} tid:{current_thread()} {car}: brumbrum        Executed')


class Car:
    def __init__(self,  id, time):
       self.id = id
       self.time = time


if __name__ == '__main__':
    
    N_CARS = 10
    N_TIME = [200, 1000, 400, 2300, 1000, 500, 1200, 1000, 2000, 40000]
    time_unix = dict()
    for i in range(N_CARS):
        print(i)
        time_unix[i] = N_TIME[i]
    #time_unix = {k: v for k, v in zip(range(N_CARS), range(N_CARS))}
    cars = [Car(f'car_{i}', time_unix[i]) for i in range(N_CARS)]
    print(cars)
    #print("interval	Object_id")
    for car in cars:
        interval = car.time  # calculate delay in seconds for execution here
        print(interval)
        #print(interval, "	", car.id)
        t = Timer(interval=interval, function=drive, args=(car.id,))
        t.start()
            
             
