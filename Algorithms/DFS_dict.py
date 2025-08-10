def dfs_iterative(graph, start):
    visited = set()
    res = []
    stack = [start]
    while len(stack) > 0:
        temp = stack.pop()
        if temp not in visited:
            visited.add(temp)
            res.append(temp)
            stack.extend(reversed(graph[temp]))   # add temp in the same order as visited
    return res
'''
      A
    B   C
   D E   F
         G


'''
graph = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['F','A'],
    'D' : ['B'],
    'E' : ['B'],
    'F' : ['C','G'],
    'G' : ['F'],
}

print(dfs_iterative(graph, 'A'))