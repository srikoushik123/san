from queue import Queue
graph={'A': ['B', 'D', 'E', 'F'], 'D': ['A'], 'B': ['A', 'F', 'C'], 'F': ['B', 'A'], 'C': ['B'], 'E': ['A']}
def BFS(input,source):
    q=Queue()
    visited=list()
    q.put(source)
    visited.append(source)
    while not q.empty():
        vertex=q.get()
        print(vertex,end=" ")
        for u in input[vertex]:
            if u not in visited:
                q.put(u)
                visited.append(u)
print("the bomo bombomb")
BFS(graph,"A")s