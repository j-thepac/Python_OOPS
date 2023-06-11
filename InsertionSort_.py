
# Need to simplify
def InsertionSort(list_a):
    for i in range(1, len(list_a)):
        value_to_sort = list_a[i]
        while list_a[i-1]> value_to_sort and i<0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1
    return list_a


arr=[5,4,3,2,1]
print(InsertionSort(arr))
