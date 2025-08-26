from multiprocessing import Process
import os

def worker():
    print(f"Process ID: {os.getpid()}")

# Create and start a process
process = Process(target=worker)
process.start()
process.join()  # Wait for the process to finish
# Advantages: Bypasses GIL, suitable for CPU-bound tasks.


