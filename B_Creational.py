"""
Factory
Singleton
builder
Prototype
"""

#*****************Factory*****************
from abc import ABC,abstractmethod
class AB(ABC):pass
class A(AB):pass
class Factory:
    def createObj(self,s:str)->AB:
        m:dict[str,AB]={"a":A}
        return m[s]
        # match s:
        #     case "a":return A()

#***************** Singleton (Single Instance )****************
#getObj shd be used to create Single Object
class Single:
    instance=None
    name="1"
    @staticmethod
    def getObj():
        if (Single.instance==None):
            Single.instance=Single()
        return Single.instance

s:Single=Single.getObj()
print(s.name)
#***************** builder *****************
# return Self ( chain methods )
class Coffee:
    price=10
    ingrediants=["sugar","milk","coffeepowder"]
    def getCoffee(self): return self

    def addCream(self):
        self.ingrediants.append("cream")
        self.price+=10
        return self

coffee:Coffee=Coffee()
print(coffee.getCoffee().addCream().ingrediants)
#*****************Prototype*****************
from copy import deepcopy
class Prototype():pass
p=Prototype()
q=deepcopy(p)

print(type(q))

