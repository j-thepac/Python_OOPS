from queue import Queue # Thread Safe 
import threading

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"Processing {item}",threading.get_native_id())
        q.task_done()
        print(f"Complted {item}",threading.get_native_id())

# Create a queue and add items
q = Queue()
for item in range(5):
    q.put(item)

# Start a worker thread
thread = threading.Thread(target=worker, args=(q,))
thread2 = threading.Thread(target=worker, args=(q,))
thread.start()
thread2.start()
q.join()  

# Wait until all tasks are done
# Advantages: Thread-safe, helps in communication between threads.
