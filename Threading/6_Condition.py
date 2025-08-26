from threading import Condition
import threading

condition = Condition()
shared_resource = []

def producer():
    with condition:
        print("Send Value")
        shared_resource.append(1)
        shared_resource.append(2)
        condition.notify(2)  # Notify the consumer
        # condition.notify()  # Notify the consumer

def consumer():
    with condition:
        while not shared_resource:  # Check if the resource is empty
            print("Conumser waiting ... ")
            condition.wait()  # Wait for the producer
        print("Consumed:", shared_resource.pop())


# Start producer and consumer threads
thread1 = threading.Thread(target=producer)
thread2 = threading.Thread(target=consumer)
thread3 = threading.Thread(target=consumer)

thread3.start()
thread2.start()
thread1.start()

thread2.join()
thread1.join()
print("Done")
# Advantages: Synchronizes threads, allows for complex interactions.
