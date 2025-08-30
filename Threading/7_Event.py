"""  
All waiting threads are unblocked once set
"""


import threading, time

event = threading.Event()

def worker_event(i):
    print(f"Worker {i} waiting...")
    event.wait()   # wait until event is set
    print(f"Worker {i} started!")

for i in range(2):
    threading.Thread(target=worker_event, args=(i,)).start()
    

time.sleep(1)
print("Main sets event")
event.set()   # all workers proceed