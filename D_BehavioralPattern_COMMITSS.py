""" COMMITSS
C-  Chain of Command ( if , elseif ,elseif)
O - Observer
M - Mediator
M - Memento
I - 
T - Template
S - Stats 
S - Strategy
"""

#Chain of Command
from abc import ABC ,abstractclassmethod
class Handler(ABC):
    def __init__(self,handle=None):
        self.handle=handle
    @abstractclassmethod
    def catchs(self,s:str):pass

class Fish(Handler):
    def catchs(self,s:str):
        if(s=="fish"):print("caught fish")
        elif (self.handle!=None):
            print(self.handle.catchs(s))


class Waste(Handler):
    def catchs(self,s:str):
        if(s=="waste"):print("caught waste")
        elif (self.handle!=None):
            print(self.handle.catchs(s))

(Fish(Waste(None))).catchs("waste")

# Observer (Youtube Notification) - Pub Sub
class Person:
    def __init__(self,name):self.name= name
    def notification(self,message):print(message)

class Observer:
    ps:list[Person]=[]
    def add_person(self,p:Person):
        self.ps.append(p)
    
    def send_notification(self,s:str):
        for p in self.ps:p.notification(s)

ram=Person("Ram")
o=Observer()
o.add_person(ram)
o.send_notification("hi")

# Mediator
class User:
    def __init__(self,name,chat:'Chat'):
        self.chat=chat
        self.name=name
        chat.add_users(self)
    def notification(self,s:str):
        print(s)
    def send_notification(self,s:str):
        self.chat.broadcast(s)

class Chat:
    usrs:list[User]=[]
    def add_users(self,usr:User):
        self.usrs.append(usr)

    def broadcast(self,s:str):
        for usr in self.usrs:
            usr.notification(s)

print("Mediator")
ch:Chat=Chat()
ram:User=User("ram",ch)
ch.add_users(ram)
ram.send_notification("hi")



# mement0
import threading
balance:int=0
class Memento:
    def __init__(self,balance:int):
        self.balance=balance

class Account:
    
    def credit(self,amt:int)->Memento:
        global balance
        memento:Memento=Memento(balance)
        lock =threading.Lock()
        lock.acquire()
        balance=balance+amt
        lock.release()
        return memento
    
    def rollback(self,memento:Memento):
        global balance
        lock =threading.Lock()
        with lock:
            balance=memento.balance

print("Memento")
acc:Account=Account()
print(f"Start Balance {balance}")
memento=acc.credit(100)
print(f"After crediting - {balance}")
acc.rollback(memento)
print(f"After roll back {balance}")

#Iterator Pattern ( Iterate an array )

# Template
from abc import ABC,abstractmethod
class Food:
    @abstractmethod
    def buy(self): pass
    @abstractmethod
    def cook(self): pass

class Pizza(Food):
    def buy(self):print("ingradiats")
    def cook(self):print("oven heat")


# Strategy Pattern
class Book:
    price:int=100
    def buy(self,coupon:str)->int:
        d={"ten":self.ten()}
        return d.get(coupon,self.price)
    def ten(self):return self.price-10

book:Book=Book()
print(book.buy('ten'))
