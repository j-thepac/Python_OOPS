
def QuickSort(arr):
    res1,res2=[],[]
    if(len(arr)==0):return arr
    else:pivot=arr.pop()
    for i in arr:
        if(i<pivot):res1.append(i)
        else:res2.append(i)
    return QuickSort(res1)+[pivot]+QuickSort(res2)

l=[5,4,3,2,1]
print(QuickSort([5,4,3,2,1]))

