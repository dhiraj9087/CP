from collections import deque
adj = [[],[2,6],[1,3,4],[2],[2,5],[4,8],[1,7,9],[6,8],[5,7],[6]]
vis = [0]*(10)
q = deque()
q.append(1)
vis[1]=1
bfs=[]
while q:
    node = q.popleft()
    bfs.append(node)
    for nei in adj[node]:
        if not vis[nei]:
            q.append(nei)
            vis[nei] = True
print(bfs)
