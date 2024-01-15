n = 10**5 + 10
g = [[] for _ in range(n)]
vis=[False]*(n)
def dfs(ind):
    # print(ind)
    vis[ind]=True
    for child in g[ind]:
        # print(ind,child)
        if vis[child]==True:
            continue
        dfs(child)
def main():
    n, m = map(int, input().split())
    for i in range(m):
        v1, v2 = map(int, input().split())
        g[v1].append(v2)
        g[v2].append(v1)
    # print(g)
    c=0
    for vertex in range(1, n + 1):
        if vis[vertex]==True:
            continue
        dfs(vertex)
        c+=1
    # print()
main()