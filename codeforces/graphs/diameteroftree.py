n = 10**5 + 10
g=[[] for i in range(n)]
depth=[0]*n
def dfs(ind,prt=-1):

    for child in g[ind]:
        if child==prt:
            continue
        depth[child]=depth[ind]+1

        dfs(child,ind)

def main():
    m=int(input())
    for i in range(m-1):
        v1,v2=map(int,input().split())
        g[v1].append(v2)
        g[v2].append(v1)
    dfs(1)
    max_depth=-1
    max_d_node = 0
    for i in range(m):
        if max_depth<depth[i]:
            max_depth=depth[i]
            max_d_node=i
        depth[i]=0
    dfs(max_d_node)
    max_depth=-1
    for i in range(m):
        if max_depth<depth[i]:
            max_depth=depth[i]
    print(max_depth)
main()