from collections import deque
adj = [[],[],[3],[1],[0,1],[0,2]]

indegree =[0]*(len(adj))
for i in range(len(adj)):
    for j in adj[i]:
        indegree[j]+=1
q=deque()
for i in range(len(indegree)):
    if indegree[i]==0:
        q.append(i)

vis = [0]*len(adj)
topo=[]
while q:
    node = q.popleft()
    topo.append(node)
    for nei in adj[node]:
        indegree[nei]-=1
        if indegree[nei]==0:
            q.append(nei)
print(topo)
