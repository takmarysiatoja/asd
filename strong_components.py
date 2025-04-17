import math


def swap(G):
    n=len(G)
    H=[[] for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            H[v].append(i)
    return H

def which(tab,val):
    for i in range(len(tab)):
        if tab[i]==val:
            return i



def components(G):                   #main
    n=len(G)
    visited=[0 for _ in range(n)]
    time=[0 for _ in range(n)]
    def DFS(u):
        visited[u]=1
        for v in G[u]:
            if visited[v]==0:
                time[v]=time[u]+1
                DFS(v)
    DFS(0)
    G=swap(G)
    visited=[0 for _ in range(n)]
    def DFS2(u):
        visited[u]=1
        for v in G[u]:
            if visited[v]==0:
                DFS2(v)
    licz=0
    for i in range(n):
        x=min(time)
        x=which(time,x)
        if visited[x]==0:
            DFS2(x)
            time[x]=math.inf
            licz+=1
    return licz


G = [
    [1],    
    [2],    
    [0],      
    [4],    
    [5],      
    [3],       
    [0]        
]

print(components(G))
