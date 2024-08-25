adj = [[],[2,3],[1,5],[1,4,6],[3],[2,7],[3,7],[5,6]]
vis=[0]*(len(adj))
flag=False
def dfs_cycle(node,parent):
    vis[node] = 1
    for nei in adj[node]:
        if not vis[nei]:
            vis[nei] = True
            if dfs_cycle(nei,node)==True:
                return True
        elif parent!=nei:
            return True
    return False
        
print(dfs_cycle(1,-1))