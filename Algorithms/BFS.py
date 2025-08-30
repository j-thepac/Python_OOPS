class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
        1
    2       3
   4 5     6 7
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

def BFS2(root):
   q,res=[],[]
   if(root == None):return None
   q.append(root)
   while q:
       lvl=[]
       for _ in range(0,len(q)):
           temp=q.pop(0)
           lvl.append(temp.data)
           if temp.left:q.append(temp.left)
           if temp.right:q.append(temp.right)
       res.append(lvl)
   return res


#Time Complexity : O(n)
def levels(root): # level Order
    if root is None:return None
    q,res=[],0
    q.append(root)
    while q:
        n=len(q)
        for _ in range(0,n):    
            temp=q.pop(0)
            if temp.left: q.append(temp.left)
            if temp.right: q.append(temp.right)
        res+=1
    return res

print(levels(root))
