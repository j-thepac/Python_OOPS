def MergeSort(arr):
    if(len(arr)==2):
        if(arr[0]>arr[1]):arr[0],arr[1]=arr[1],arr[0]
        return arr
    elif(len(arr)==1):return arr
    else:
        mid=len(arr)//2
        MergeSort(arr[0:mid])
        MergeSort(arr[mid:])
    res=[]
    

l=[3,4,1,2,8,9]
res=MergeSort(l)
print(res)
