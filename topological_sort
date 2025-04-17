def topo(G):
    n=len(G)
    visited=[0 for _ in range(n)]
    t=[]
    def DFS(u):
        if visited[u]==0:
            visited[u]=1 
            for v in G[u]:
                DFS(v)
            t.append(u)
    for i in range(n):
        DFS(i)
    return t[::-1]
G = [
    [],         # 0
    [],         # 1
    [3],        # 2
    [1],        # 3
    [0, 1],     # 4
    [0, 2]      # 5
]
print(topo(G))
