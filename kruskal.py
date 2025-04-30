class Node:
    def __init__(self,val):
        self.parent=self
        self.value=val
        self.rank=0

def find(x):
    if x!=x.parent:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if x.rank<y.rank:
        x.parent=y
    else:
        y.parent=x
        if y.rank==x.rank:
            x.rank+=1

def to_node(x):
    head=Node(x)
    head.parent=head
    return head

def kruskal(G):
    n=len(G)
    edges=[]
    A=[]
    sets=[None for _ in range(n)]
    for a in range(n):
        for b,c in G[a]:
            edges.append((a,b,c))
    edges.sort(key=lambda x: x[2])
    for v in range(n):
        sets[v]=to_node(v)
    for e in edges:
        a,b,c=e
        if find(sets[a])!=find(sets[b]):
            A.append(e)
            union(sets[a],sets[b])
    return A
