## Fibnocci
#-----------Normal---------------
n=5
l=[0,1]
for i in range(n-2):l.append(l[-1]+l[-2])
print(l)
#-----------Recursion (exit+change state+self call)----
def fib(n):
    if n==0:return 0
    elif n==1: return 1
    return fib(n-1)+fib(n-2)
res=[]
for i in range(0,5):res.append(fib(i))
print(res)
#---------Memoization (store intermitten result)------------
d={}
def fib(n):
    if n==0:return 0
    elif n==1: return 1
    if(n not in d): d[n]=fib(n-1)+fib(n-2)
    return d[n]
n=5
res=[]
for i in range(0,5):res.append(fib(i))
print(res)
#------------ BackTracking (recursion+tempRes+delete) ---------------------
def fib(n,tempRes=[]):
    if(n==0): 
        tempRes.append(0)
        return 0
    elif(n==1): 
        tempRes.append(1)
        return 1
    x=fib(n-1,tempRes)+fib(n-2,tempRes)
    tempRes.append(x)
    return x

def fn():
    res=[]
    tempRes=[]
    for i in range(0,5):
        fib(i,tempRes)
        res.append(tempRes.pop())
    return res
print(fn())

