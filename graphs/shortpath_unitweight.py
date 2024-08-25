from collections import deque
from math import inf


adj = [[1,3],[0,2,3],[1,6],[0,4],[3,5],[4,6],[2,5,7,8],[6,8],[6,7]]
distance = [inf]*len(adj)
q=deque()
q.append([0,0])
distance[0]=0

while q:
    node,dist = q.popleft()
    for nei in adj[node]:
        if (dist+1) < distance[nei]:
            distance[nei]=dist+1
            q.append([nei,dist+1])
print(distance)