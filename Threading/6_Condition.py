"""
You want to wake up specific threads selectively
producer–consumer
 """
condition = threading.Condition()
items = []

def consumer():
    with condition:
        while not items:        # must check in loop
            print("Consumer waiting...")
            condition.wait()
        print("Consumer got:", items.pop())

def producer():
    time.sleep(1)
    with condition:
        items.append("apple")
        print("Producer added item")
        condition.notify()

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()