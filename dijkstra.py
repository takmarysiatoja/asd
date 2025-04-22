from math import inf
from queue import PriorityQueue

def dijkstra(G,a):
    n=len(G)
    dist=[inf for _ in range(n)]
    parent=[-1 for _ in range(n)]
    visited=[0 for _ in range(n)]
    Q=PriorityQueue()

    def Relax(u,v,w):
        if dist[u]+w<dist[v]:
            dist[v]=dist[u]+w
            parent[v]=u
            Q.put((dist[v],v))

    dist[a]=0
    Q.put((dist[a],a))
    while not Q.empty():
        d,u=Q.get()
        if not visited[u]:
            visited[u]=True
            for v,w in G[u]:
                Relax(u,v,w)
    return dist,parent

G = [
    [(1, 10), (5, 9999)],
    [(0, 10), (2, 10)],
    [(1, 10), (3, 10)],
    [(2, 10), (4, 10)],
    [(3, 10), (5, 9999)],
    [(0, 9999), (4, 9999)]
]

print(dijkstra(G, 0))
