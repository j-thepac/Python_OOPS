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