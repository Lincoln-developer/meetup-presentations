# example of using the queue
from threading import Thread
from time import sleep
from random import random
from queue import Queue

# generate work
def producer(queue):
    print("Producer: Running")
    # generate work
    for i in range(10):
        # generate value
        value = random()
        # block for a moment
        sleep(value)
        # add to the queue
        queue.put(value)
    
    # all done
    queue.put(None)
    print("Producer: Done")

# consumer work
def consumer(queue):
    print("Consumer: Running")
    # consumer worker
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        # report
        print(f">got {item}")

    # all done
    print("Consumer: Done")

# create the shared queue
queue = Queue()

# start the consumer
_consumer = Thread(target=consumer, args=(queue, ))
_consumer.start()

# start the producer
_producer = Thread(target=producer, args=(queue, ))
_producer.start()

# wait for all threads to finish
_consumer.join()
_producer.join()