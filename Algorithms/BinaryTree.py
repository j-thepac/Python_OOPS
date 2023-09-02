class BinaryTree:
    def __init__(self,i):
        self.i=i
        self.left:BinaryTree=None
        self.right:BinaryTree=None

    def append(self,i):
        if(i<self.i):
            if(self.left==None):self.left=BinaryTree(i)
            else:self.left.append(i)
        else:
            if(self.right==None):self.right=BinaryTree(i)
            else:self.right.append(i)

    def find(self,i):
        if(self.i==i):print(i)
        elif(i<self.i):
            if(self.left!=None):self.left.find(i)
        elif(i>self.i):
            if(self.right!=None):self.right.find(i)
        else:print("Not Found")

    def preRoot(self):  #Root > Left > Right
        print(self.i)
        if(self.left):self.left.preRoot()
        if(self.right):self.right.preRoot()

    def postRoot(self): #left>Right>Root
        if(self.left):self.left.postRoot()
        if(self.right):self.right.postRoot()
        print(self.i)

    def inRoot(self):
        if(self.left):self.left.inRoot()
        print(self.i)
        if(self.right):self.right.inRoot()

def preRoot2(root):
    if root is None:return
    print(root.i)
    preRoot2(root.left)
    preRoot2(root.right)


bt=BinaryTree(10)
for i in [5,15,4,6,16,14,3]:bt.append(i)

