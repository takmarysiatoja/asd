from math import inf


def bellman_ford(G,s):
    n=len(G)
    dist=[inf for _ in range(n)]
    parent=[-1 for _ in range(n)]
    dist[s]=0
  
    def relax(u,v,w):
        if dist[u]+w<dist[v]:
            dist[v]=dist[u]+w
            parent[v]=u
          
    for i in range(n):
        for (v,w) in G[i]:
            relax(i,v,w)
          
    for i in range(n):
        for (v,w) in G[i]:
            if dist[v]>w+dist[i]:
                return "cykl ujemny istnieje"
              
    return dist,parent
