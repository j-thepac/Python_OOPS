def rev(l):
    n=len(l)
    for i in range(0, n//2):
        l[i], l[n - i - 1] = l[n - i - 1], l[i]
    
l = [1, 2, 3]
rev(l) 
print(l)
