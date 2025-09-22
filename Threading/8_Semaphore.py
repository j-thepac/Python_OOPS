from threading import Semaphore
import time
import threading

semaphore = Semaphore(2) # Max 2 thread at a time

def access_resource():
    with semaphore:
        print("Accessing resource")
        time.sleep(1)  # Simulate resource access

# Start multiple threads
threads = [threading.Thread(target=access_resource) for _ in range(5)]
for thread in threads:
    thread.start()
# Advantages: Controls access to a shared resource, limits concurrent access.
