def Search(arr,value):
    mid=len(arr)//2
    if(len(arr)==0):
        print("Not Found")
        return
    if(arr[mid]==value): print("Found")
    elif(value<arr[mid]):Search(arr[0:mid],value)
    elif(value>arr[mid]):Search(arr[mid+1:],value)

arr=list(range(0,20))
st=sorted(arr)
print(st)
Search(st,14)
