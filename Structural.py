""" ABCDFFP
Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy
"""
# Adapter
class Socket:
    v=230
class Toaster:
    def on(self,s:Socket):
        if(s.v>110):print("blast")
class Adapter(Socket):
    v=110
    def __init__(self,t:Toaster):pass
Toaster().on(Adapter(Socket()))

# Bridge
from abc import ABC,abstractmethod
class Color(ABC):
    @abstractmethod
    def paint(self):pass
class Pattern(ABC):
    @abstractmethod
    def draw(self,cm:int,c:Color):pass

class Red(Color):
    def paint(self):return ("Red")
class Circle(Pattern):
    def draw(self,cm,c:Color):print(c.paint(),cm)
Circle().draw(5,Red())

# Composite
class Dog(ABC):
    @abstractmethod
    def bark(self):pass
class Dogs(Dog):
    dogs:list[Dog]=[]
    def addDog(self,dog:Dog):self.dogs.append(dog)
    def bark(self):
        for dog in self.dogs:dog.bark()
class Pommerian(Dog):
    def bark(self):print("wof")

shelter=Dogs()
tommy=Pommerian()
shelter.addDog(tommy)
shelter.bark()

#Decorator
from dataclasses import dataclass
@dataclass(init=True)
class Coffee():
    price:int
    ingrediants:list[str]
class CoffeeDay():
    def getCoffee(self):return Coffee(10,["sugar","milk","coffee"])
    def addCream(self,c:Coffee):return Coffee(c.price+10,[*c.ingrediants,"cream"])

cday=CoffeeDay()
print(cday.addCream(cday.getCoffee()))

# Facade
class CPU:
    print("cpu: 1.8ghz")
class Memory:
    print("mem: DDR4 500GB")
class Computer:
    CPU()
    Memory()
Computer()

# FlyWeight
