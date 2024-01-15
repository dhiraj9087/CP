n,m=map(int,input().split())
maxi=10
g1=[[0 for j in range(maxi)]for i in range(maxi)]
g2=[[]]*n
for i in range(m):
    v1,v2=map(int,input().split())
    g1[v1][v2]=1
    g1[v2][v1]=1
    g2[v1].append(v2)
print(g2)
