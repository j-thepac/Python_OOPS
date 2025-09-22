
import threading
import time

def worker():
    print("Thread starting")
    time.sleep(1)  # Simulate work
    print("Thread finished")

# Create and start multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=worker)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
# Advantages: Lightweight, easy to implement for I/O-bound tasks, allows concurrent execution.
