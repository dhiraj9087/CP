def dfs(node,vis,adj,ans):
    vis[node] = 1
    ans.append(node)
    for nei in adj[node]:
        if not vis[nei]:
            dfs(nei,vis,adj,ans)



adj = [[],[2,3],[1,5,6],[1,4,7],[3,8],[2],[2],[3,8],[4,7]]
vis = [0]*(10)
vis[1] = 1
ans=[]
ans.append(1)
dfs(1,vis,adj,ans)
print(ans)