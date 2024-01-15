import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    g=[[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v=map(int,input().split())
        g[u].append(v)
        g[v].append(u)
    leaf=[]
    for i in range(1,len(g)):
        if len(g[i])==1:
            leaf.append(i)
    # print(leaf)
    for i in range(len(g)):
        for j in range(len(leaf)):
            if leaf[j] in g[i] and 1 in g[i]:
                print(len(leaf)-1)
                return
    leaf=[0]*n
    dis=[float('inf')]*n
    depth=[0]*n
    def dfs(ind,prt):

        for child in g[ind]:

            if child==prt:
                continue
            f=0
            depth[child]=depth[ind]+1
            dfs(child,ind)
            dis[ind]=min(dis[ind],dis[child]+1)
            leaf[ind]+=leaf[child]
        if f:
            leaf[ind]=1
            dis[ind]=1
    dfs(0,-1)
    ans=0
    for i in range(n):
        if dis[i] != 0  and dis[i]<=depth[i]:
            ans=max(ans,leaf[i])
    print(ans)
            # height[ind] = max(height[ind],height[child]+1)
    
    # for i in g:
    #     if 1 in i and 
    # print(1)
for _ in range(int(input())):
   main()
