from threading import Event
import threading
event = Event()

def wait_for_event():
    print("Waiting for event...")
    event.wait()  # Block until the event is set
    print("Event occurred!")

# Start a thread that waits for the event
thread = threading.Thread(target=wait_for_event)
thread2 = threading.Thread(target=wait_for_event)
thread.start()
thread2.start()
event.set()  # Trigger the event
# Advantages: Simple way to signal between threads.
