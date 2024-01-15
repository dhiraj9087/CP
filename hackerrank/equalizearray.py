n=int(input())
q=[]
a=list(map(int,input().split()))
for i in range(len(a)):
    q.append(a.count(a[i]))
print(n-max(q))
