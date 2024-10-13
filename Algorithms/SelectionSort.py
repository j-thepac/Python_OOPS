def fn(l):
    for i in range(0,len(l)):
        for j in range(i,len(l)):   
            if l[j]<l[i]:
                l[j],l[i]=l[i],l[j]              
    return l

print(fn([5,4,3,2,1]))