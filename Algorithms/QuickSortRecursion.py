def fn(l):
    if l==[] or len(l)==0 or l==None:return []
    m1,m2=[],[]
    x=l.pop()
    for i in l:
        if(i<x):m1.append(i)
        elif(i>=x):m2.append(i)
    return fn(m1)+[x]+fn(m2)

print(fn([5,4,4,3,2,1]))