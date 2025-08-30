import threading
from concurrent.futures import *
import queue
import time 

balance=0
q =         queue.Queue()
condition=  threading.Condition()
lock =      threading.Lock()
event =     threading.Event()
sema=       threading.Semaphore(1)

def bank():
    event.wait() 
    global balance
    with condition:
        with sema:
            while q.empty(): 
                condition.wait()
                amt=q.get()
                balance+=amt
                print(f"received:{amt} bal:{balance}")

def cust(money):
    event.wait() 
    with condition:
        q.put(money)
        print(f"sent {money}")
        condition.notify()

u1=threading.Thread(target=cust,args=(100,))
u2=threading.Thread(target=cust,args=(-10,))
bnk=threading.Thread(target=bank)
u1.start()
bnk.start()
u2.start()


print("operation starts now")
time.sleep(0.5)
event.set() 
