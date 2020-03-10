class Node:
    def __init__(self, state, parent, actions):
        self.state = state
        self.parent = parent
        self.actions = actions

graph = {
        'A': Node('A', None, ['B','F','C']),
        'B': Node('B', None, ['A','C','D']),
        'C': Node('C', None, ['A','B','D','F']),
        'D': Node('D', None, ['B','E','C']),
        'E': Node('E', None, ['D','F']),
        'F': Node('F', None, ['A','C','E'])
        }

# visited = {}
def printAllPathsUtil(g, u, d, visited, path): 
        visited[u]= True
        path.append(u) 
        if u ==d:
            for i in path:
                if(i != path[-1]):
                    print (i + " -> ", end='')
                else:
                    print(i)
        else: 
            for i in g[u].actions: 
                if visited[i]==False: 
                    printAllPathsUtil(g, i, d, visited, path) 
        path.pop() 
        visited[u]= False

def printAllPaths(g, s, d): 
    visited = {'A':False,'B':False,'C':False,'D':False,'E':False,'F':False,} 
    path = [] 
    printAllPathsUtil(g, s, d, visited, path)

printAllPaths(graph,'A','E')
