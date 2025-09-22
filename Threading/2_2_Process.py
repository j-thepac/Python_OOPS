import multiprocessing as mp
import time

def worker(worker_id, barrier, condition, event, queue, semaphore):
    with semaphore: # Semaphore: Limit concurrent access
        print(f"Worker {worker_id}: Starting work")
        time.sleep(1)
    
    barrier.wait()  # Barrier: Wait for all processes to reach this point
    print(f"Worker {worker_id}: Passed barrier")
    queue.put(f"Result from worker {worker_id}")
    if worker_id == 2:event.set() # Event: set by last process
    event.wait()  # Event: Wait for signal (simpler approach)
    print(f"Worker {worker_id}: All done!")

if __name__ == '__main__':
    # Initialize synchronization objects
    barrier = mp.Barrier(3)
    condition = mp.Condition()
    event = mp.Event()
    queue = mp.Queue()
    semaphore = mp.Semaphore(2)  # Allow 2 concurrent workers
    
    # Create and start processes
    processes = [mp.Process(target=worker, args=(i, barrier, condition, event, queue, semaphore)) for i in range(3)]
    for p in processes: p.start()
    
    # Collect results from queue
    for _ in range(3):
        print(f"Main: {queue.get()}")
    
    for p in processes: p.join()