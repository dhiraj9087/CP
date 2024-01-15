
n = 10**5 + 10
g = [[] for _ in range(n)]
# vis=[False]*(n)
depth=[0]*n
height=[0]*n
def dfs(ind,prt):
    for child in g[ind]:
        if child==prt:
            continue
        depth[child]=depth[ind]+1
        dfs(child,ind)
        height[ind] = max(height[ind],height[child]+1)
def main():
    global n, m
    m = int(input())
    
    for i in range(m):
        v1, v2 = map(int, input().split())
        g[v1].append(v2)
        g[v2].append(v1)

    # print(g)
    dfs(1,0)
    for i in range(m):
        print(depth[i],height[i])
    
main()
            