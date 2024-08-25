from collections import deque
# n = 10**5 + 10
# g = [[] for _ in range(n)]
# vis=[False]*(n)
# def dfs(ind,prt):
#     vis[ind]=True
#     isloopexit=False
#     for child in g[ind]:
#         if vis[child]==True and child==prt:
#             continue
#         if vis[child]==True:
#             return True
#         isloopexit|=dfs(child,ind)
#     return isloopexit
# def main():
#     n, m = map(int, input().split())
#     for i in range(m):
#         v1, v2 = map(int, input().split())
#         g[v1].append(v2)
#         g[v2].append(v1)
#     c=0
#     flag=False
#     for vertex in range(1, n + 1):
#         if vis[vertex]==True:
#             continue
#         if dfs(vertex,0):
#             flag=True
#             break
#     return flag
# print(main())

adj = [[],[2,3],[1,5],[1,4,6],[3],[2,7],[3,7],[5,6]]

q=deque()
vis=[0]*(len(adj))
bfs=[]

q.append([1,-1])
vis[1] = 1
flag=False
while q:
    node,parent = q.popleft()
    # bfs.append(node)
    for nei in adj[node]:
        if not vis[node]:
            q.append([nei,node])
            vis[node] = True
        elif parent!=nei:
            flag=True
print(flag)
