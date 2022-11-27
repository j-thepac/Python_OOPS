"""
Factory
Singleton
builder
Prototype
"""
#Factory
from abc import ABC,abstractmethod
class AB(ABC):pass
class A(AB):pass
class Factory:
    def createObj(self,s:str)->AB:
        m:dict[str,AB]={"a":A}
        return m[s]
        # match s:
        #     case "a":return A()

#Singleton
#builder : No type of constructor parameters hence builder by Default
#Prototype
from copy import deepcopy
class Prototype():pass
p=Prototype()
q=deepcopy(p)

print(type(q))

