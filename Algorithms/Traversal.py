class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def BFS(self,root):
        if root is None: return
        queue = [root]
        while queue:
            node = queue.pop(0)  
            print(node.value, end=' ')  
            if node.left:queue.append(node.left)
            if node.right:queue.append(node.right)

    def DFS(self,node):
        if node is None:return
        print(node.value, end=' ')
        self.DFS(node.left)
        self.DFS(node.right)

    def DFS_graph(self,graph, start):
        visited = set()  
        stack = [start]  
        while stack:
            node = stack.pop()  
            if node not in visited:
                visited.add(node)  
                print(node, end=' ')  
                stack.extend(graph[node])  

    def BFS_graph(self,graph, start):
        visited = set() 
        queue = [start] 
        while queue:
            node = queue.pop(0)  
            if node not in visited:
                visited.add(node)  
                print(node, end=' ') 
                queue.extend(graph[node])  

'''
     1
    2 3
   4 5 

'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.DFS(root)  # Output: 1 2 4 5 3
print()
root.BFS(root)
print()
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

root.BFS_graph(graph, 'A')  # Output: A B C D E F
print()
root.DFS_graph(graph, 'A')  # Output: A C F E B D