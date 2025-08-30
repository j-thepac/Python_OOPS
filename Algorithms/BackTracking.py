#permutations
res = []
def fn(A,res,subset,index):
    res.append(subset[:])
    for i in range(index,len(A)):
        subset.append(A[i])
        fn(A, res, subset, i + 1)
        subset.pop()

fn([1, 2], res, [], 0)
print(res)

  



