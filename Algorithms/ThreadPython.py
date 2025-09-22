
import threading
import time
balance: int =100
class Bank():
    def credit(self,amt:int):
        global balance
        # lock =threading.Lock
        # lock.acquire()
        time.sleep(5)
        balance=balance+amt
        # lock.release()

    def debit(self,amt:int):
        global balance
        # lock =threading.Lock
        # lock.acquire()
        time.sleep(2)
        balance=balance-amt
        # lock.release()    

bank=Bank()    
t=threading.Thread(target=bank.credit,args=(100,))
t.start()
t2=threading.Thread(target=bank.debit,args=(200,))
t2.start()
print(balance)
t.join()
print(balance)
t2.join()
print(balance)


# import threading 
# deposit = 100

# def add_profit(): 
#     global deposit
#     lock= threading.Lock()
#     for i in range(100):
#         lock.acquire()
#         deposit = deposit + 10
#         lock.release()

# def pay_bill(): 
#     global deposit
#     lock= threading.Lock()
#     for i in range(100):
#         lock.acquire()
#         deposit = deposit - 10
#         lock.release()
        
# thread1 = threading.Thread(target = add_profit, args = ())
# thread2 = threading.Thread(target = pay_bill, args = ())
# thread1.start() 
# thread2.start() 
# thread1.join()
# thread2.join()
# print(deposit)
