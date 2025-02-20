# example of a mutual exclusion (mutex) loc
from time import sleep
from random import random
from threading import Thread
from threading import Lock

# work function
def _task_function(lock, identifier, value):
    # acquire the lock
    with lock:
        print(f">thread {identifier} got the lock, sleeping for {value}")
        sleep(value)

# create a shared lock
lock = Lock()

# start a few threads that attempt to execute the same critical section
for i in range(10):
    # start a thread
    Thread(target=_task_function, args=(lock, i, random())).start()
