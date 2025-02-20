# example of running a function in another thread
from time import sleep
from threading import Thread

# a custom function that blocks for a moment
def custom_function():
    # block for a moment
    sleep(1)
    # display a message
    print("This is from another thread")

# create a thread instance
thread = Thread(target=custom_function)

# run the thread
thread.start()

# wait for the thread to finish
print("Waiting for the thread to finish...")
thread.join()