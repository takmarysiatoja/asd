from collections import deque
from math import inf

def BFS(G,s):
    n=len(G)
    Q=deque()
    Q.append(s)
    visited=[False for _ in range(n)]
    parent=[-1 for _ in range(n)]
    dist=[inf for _ in range(n)]
    dist[s]=0
    visited[s]=True
    while Q:
        u=Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                dist[v]=dist[u]+1
                Q.append(v)
    return parent,dist

