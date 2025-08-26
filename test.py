
"""The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved.
"""
def kata_13_december(lst): 
    # Fix this code
    i=0
    while i<len(lst):
        if lst[i]%2 ==0: 
            del lst[i]
        else:i+=1
    return lst
assert(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]), [1, 3, 5, 7])


