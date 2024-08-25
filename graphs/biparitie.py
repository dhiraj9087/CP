from collections import deque


graph=[[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
col=[-1]*(len(graph))

def bi():
    q=deque()
    q.append(0)
    col[0]=0
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if col[nei]==-1:
                col[nei] = 1-col[node]
                q.append(nei)
            if col[nei]==col[node]:
                return False
    return True

for i in range(len(col)):
    if col[i]==-1:
       if bi()==False:
           print(False)
           break

print(True)