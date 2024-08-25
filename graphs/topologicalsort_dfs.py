# Topological sort is an ordering of the vertices (or nodes) in a directed acyclic graph (DAG) such that for every directed edge 
# (𝑢,𝑣)(u,v), vertex 𝑢 comes before vertex 𝑣 in the ordering. This type of ordering is possible only if the graph has no cycles (i.e., it is acyclic).

adj = [[],[],[3],[1],[0,1],[0,2]]
def topo(node,stack):
    vis[node]=1
    for nei in adj[node]:
        if vis[nei]==0:
            topo(nei,stack)
    stack.append(node)

vis=[0]*(len(adj))
stack =[]
for i in range(len(adj)):
    if vis[i]==0:
        topo(i,stack)
print(stack[::-1])