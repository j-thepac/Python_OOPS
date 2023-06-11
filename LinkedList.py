"""
- Uses Recurssion ( No Calculation done until base is reached)
- Lot of Function calls for large Dataset lead to Out Of Memory
- Always Start code with exit Condition First eg:if(n==1):return 1
"""

class LinkedList:
    def __init__(self,i):
        self.i=i
        self.nxt:LinkedList=None

    def append(self,i):
        if(self.nxt==None):self.nxt=LinkedList(i)
        else:self.nxt.append(i)

    def display(self):
        if(self.nxt!=None):
            print(self.i)
            self.nxt.display()
        else:print(self.i)

    def reverseDisplay(self):
        if(self.nxt!=None):
            self.nxt.display()
            print(self.i)
        else:print(self.i)

    def remove(self,i):
        if(self.i==i):                      #1st ele
            self.i=None
            self.nxt=None
        elif(self.nxt==None):print("Not Found") #last ele
        else:                                   #Middle
            if(self.nxt.i==i):self.nxt=self.nxt.nxt
            else:self.nxt.remove(i)

    def change(self,i,j):
        if(self.i==i):
            self.i=j
        elif(self.nxt==None):print("Not Found")
        else:self.nxt.change(i,j)

def upDateIndex(lnkdlst, index, value):
    temp=lnkdlst.nxt
    for i in range(1,index):temp=temp.nxt
    temp.i=value
    return lnkdlst

ll=LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.change(2,100)
ll.display()
