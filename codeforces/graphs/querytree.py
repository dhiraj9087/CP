n = 10**5 + 10
g = [[] for _ in range(n)]
# vis=[False]*(n)
subtree_sum=[0]*n
even_count=[0]*n
def dfs(ind,prt):
    if ind%2==0:
        even_count[ind]+=1
    subtree_sum[ind]+=ind
    for child in g[ind]:

        if child==prt:
            continue
        
        dfs(child,ind)
        subtree_sum[ind]+=subtree_sum[child]
        even_count[ind]+=even_count[child]
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
        print(subtree_sum[i],even_count[i])
    
main()
            