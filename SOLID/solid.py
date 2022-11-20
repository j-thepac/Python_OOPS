
# Single Responsibility
class File:
    def save(self):pass

class Person:
    def name(self):pass

# Open Closed
class Book:
    price:float=100
    def get_price(self):return self.price

class Diwali_Book(Book):
    def get_price(self):return self.price*0.1


# Liskov Inversion
from abc import abstractmethod,ABC
class Bird(ABC):pass

class Penguine(Bird):
    def eat(self):return "fish"

class FlyingBird(Bird):
    def fly(self):return True

class Eagle(FlyingBird):
    def eat(self): return "carnivore"
  
# Interface Segregation
class Radio(ABC):
    def play(self): return("song")

class Telephone(ABC):
    def call(self):return ("call")

class Mobile(Radio,Telephone):pass


# Dependency Inversion
#-----normally---------------
class QA:pass
class Manager:
    qas:list[QA]
    def add_qa(self,qa:QA):self.qas.append(QA)
#------ With Dependency Inversion------
class Emp:pass
class Dev(Emp):pass
class BA(Emp):pass

class ManagerNew:
    emps:list[Emp]
    def addEmp(self,emp:Emp):self.emps.append(emp)



