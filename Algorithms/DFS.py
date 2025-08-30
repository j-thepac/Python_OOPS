"""
       1
   2       3
  4 5     6 7
"""
class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def DFS(root,start):
    q=[root]
    res=set()
    while q !=[]:
        temp=q.pop()
        if temp.data not in res:res.add(temp.data)
        if(temp.left !=None): q.append(temp.left)
        if(temp.right !=None): q.append(temp.right)
    return res
print(DFS(root,'A'))