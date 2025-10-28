graph={}
edge_set=set()
def add_node(node):
    if node in graph:
        printf(f"'{node}' already exists.Please enter a different node")
        return False
    graph[node]=[]
    return True
def add_edge(u,v):
    edge=tuple(sorted((u,v)))
    if edge in edge_set:
        print(f"Edge {u}-{v} already exists.Please enter a different edge")
        return False
    if u not in graph or v not in graph:
        print("Both nodes must be added before connecting them with edges")
        return False
    graph[u].append(v)
    graph[v].append(u)
    edge_set.add(edge)
    return True
def bfs(start):
    visited=[]
    queue=[start]
    print("BFS:",end=" ")
    while queue:
        node=queue.pop(0)
        if node not in visited:
            print(node,end=" ")
            visited.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    print()
def dfs(node,visited=None):
    if visited is None:
        visited=[]
        print("DFS:",end=" ")
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(neighbour,visited)
n=int(input("Enter number of nodes:"))
i=0
while i<n:
    node=input(f"Enter node {i+1}:").strip()
    if add_node(node):
        i+=1
e=int(input("Enter the number of edges:"))
for i in range(e):
    while True:
        u,v=input(f"Enter edge {i+1} (two nodes):").split()
        if add_edge(u,v):
            break
start=input("Enter the starting node:").strip()
if start in graph:
    bfs(start)
    dfs(start)
    print()
else:
    print("Starting node not found in graph")
