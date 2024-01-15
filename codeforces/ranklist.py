n,k=map(int,input().split())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    d.append((a,b))
# print(d)
# d.sort(key=)
for i in range(len(d)):
    for j in range(0,len(d)-i-1):
        if d[j][0]<d[j+1][0]:
            d[j],d[j+1]=d[j+1],d[j]
# print(d)
for i in range(len(d)):
    for j in range(0,len(d)-i-1):
        # print(i,j)
        if d[j][0]==d[j+1][0] and d[j][1]>d[j+1][1]:
            d[j],d[j+1]=d[j+1],d[j]
# print(d)
print(d.count(d[k-1]))
