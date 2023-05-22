
"""
   we define a new class that extends the threading.Thread class,
   define the instance variable in the constructor and set it to
   None, then override the run() function with custom code and set
   the  instance variable. The main thread will then access the return value
"""
from time import sleep
from threading import Thread

# custom thread class
class CustomThread(Thread):
    # constructor
    def __init__(self):
        # execute the base constructor
        Thread.__init__(self)
        # set a default value
        self.value = None
    
    # function executed in a new thread
    def run(self):
        # block for a moment
        sleep(1)
        # store data in an instance variable
        self.value = "Hello Pythonista, we are returning data from a new thread."

# create a new thread
thread = CustomThread()

# start the thread
thread.start()

# wait for the thread to finish
thread.join()

# get the value returned from the thread
data = thread.value
print(data)

