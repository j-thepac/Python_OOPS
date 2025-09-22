from threading import Timer

def hello():
    print("Hello, world!")

# Set a timer to call hello after 2 seconds
timer = Timer(2.0, hello)
timer.start()
# Advantages: Delayed execution of a function, useful for scheduling tasks.
