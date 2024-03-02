edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]
signalSpeed = 1
n=len(edges)
g=[[0] for i in range(10000)]
# c=
# for i,j,k in edges:
#     g[i].append(j)
#     g[j].append(i)
for i in range(n):
    g[edges[i][0]]=[edges[i][1],edges[i][0]+edges[i][2]]
print(g)