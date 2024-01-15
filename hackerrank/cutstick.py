a=int(input())
b=list(map(int,str(input()).split()))
for i in range(len(b)):
    if len(b)>0:
        m=min(b)
        b=[i-m for i in b]
        print(len(b))
        c=b.count(0)
        for j in range(c):
            b.remove(0)