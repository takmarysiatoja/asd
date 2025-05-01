#only for directed graphs

from copy import deepcopy

def euler(G):
    H=deepcopy(G)
    t=[]
    def DFS(u):
        t.append(u)
        l=len(H[u])
        for i in range(l):
            if H[u][i] is not None:
                x=H[u][i]
                H[u][i]=None
                DFS(x)
    DFS(0)
    return t 
