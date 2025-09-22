from threading import Barrier
import threading 
barrier = Barrier(3)

def wait_at_barrier():
    print("Waiting at barrier")
    barrier.wait()  # Block until all threads reach the barrier
    print("Crossed barrier")

# Start multiple threads
threads = [threading.Thread(target=wait_at_barrier) for _ in range(3)]
for thread in threads:
    thread.start()
# Advantages: Synchronizes a fixed number of threads at a point.
