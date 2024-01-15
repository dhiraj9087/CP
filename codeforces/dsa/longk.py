from collections import defaultdict
str = "1432543214325432"
K = 5
d={}
n=len(str)
q=0
for i in range(n-K):
    a=str[i:i+K]
    d[a]=0
for i in range(n-K):
    a=str[i:i+K]
    d[a]+=1
# print(d)
for i in d:
    if d[i]>1:
        print(i,d[i])
