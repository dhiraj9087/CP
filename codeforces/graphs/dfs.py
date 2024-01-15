n = 10**5 + 10
g = [[] for _ in range(n)]
vis=[False]*(n)
def dfs(ind):

    vis[ind]=True
    for child in g[ind]:

        if not vis[child]:
            continue

        dfs(child)


def main():
    global n, m
    n, m = map(int, input().split())
    
    for i in range(m):
        v1, v2 = map(int, input().split())
        g[v1].append(v2)
        g[v2].append(v1)

    # print(g)
    for vertex in range(1, n + 1):
        if not vis[vertex]:
            dfs(vertex)
main()