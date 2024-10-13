r = [""]  
v = "abcd"  
for i in v:
    temp = []  
    for j in r:
        temp.append(i + j)
    r.extend(temp)  

print(r)