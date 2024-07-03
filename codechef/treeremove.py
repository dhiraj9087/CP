import math
import sys
input=sys.stdin.readline
import collections
def main():
    n = int(input())
    g = [[] for _ in range(n)]
    a = list(map(int, input().split()))
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    
    ind = a.index(min(a))
    vis = [False] * n
    order = [ind]
    vis[ind] = True
    bfs = collections.deque([ind])
    
    while bfs:
        node = bfs.popleft()
        for neighbor in g[node]:
            if not vis[neighbor]:
                vis[neighbor] = True
                order.append(neighbor)
                bfs.append(neighbor)
    
    ans = order[1:][::-1]
    ans = [i + 1 for i in ans]
    print(len(ans))
    print(*ans)


for _ in range(int(input())):
   main()
