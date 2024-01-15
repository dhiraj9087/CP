def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a1=[0]*n
    a2=set()
    d={}
    c=0
    for i in range(n-1,-1,-1):
        if a[i] not in a2:
            a2.add(a[i])
            c+=1
            a1[i]=c
        else:
            a1[i]=c
        # d[i+1]=len(set(a[i::]))
    # print(d)
    # print(a1,a2)
    w=[]
    for i in range(m):
        q=int(input())
        w.append(a1[q-1])
        # print(d[q])
    print(*w,sep='\n')

solve()


