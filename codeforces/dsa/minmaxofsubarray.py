# a=[3,2,4,5,6,1,9]
a=[1,2,3,3,2,2]
k=3
q=[]
n=len(a)
for i in range(n-k):
    m=a[i:i+k]
    q.append(m)
print(q)
s=[]
for i in range(len(q)):
    s.append(max(q[i])-min(q[i]))
print(min(s))
