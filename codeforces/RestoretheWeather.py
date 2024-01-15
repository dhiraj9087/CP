def solve():
    # n,k=map(int,input().split())
    # a=list(map(int,input().split()))
    # b=list(map(int,input().split()))
    # b.sort()
    # print(b)
    # for i in range(n-1):
    #     if abs(a[i]-b[i])>k:
    #         b[i],b[i+1]=b[i+1],b[i]
    # print(b)
    # c=0
    # for i in range(n):
    #     if abs(a[i]-b[i])<=k:
    #         c+=1
    # print(c)
    # c=[abs(a[i]-b[i]) for i in range(n)]
    # print(c)
    # d=[]
    # for i in range(n):
    #     if c[i]>k:
    #         d.append(i)
    # print(d)
    # c=[]
    # for i in range(n):
    #     for j in range(i,n):
    #         if a[i]+k>b[j]:
    #             c.append(b[i])
    #             break
    #         # else:
    # print(c)
    # a.sort()
    # v=[]
    # for i in range(n):
    #     v.append([a[i],i])
    # print(v)
    # v.sort()
    # print(v)
    # b.sort()
    # print(*b)
    # c=[0]*n
    # for i in range(n):
    #     c[v[i][1]] = b[i]
    # print(c)
    # b.sort()
    # d=[]
    # for i in range(n):
    #     d.append((a[i],b[i]))
    # for i in range(n):
    #     print(d[i][1],end=' ')
    # print()
    # n, k = map(int, input().split())
    # a = [(int(input()), i) for i in range(n)]
    # b = list(map(int, input().split()))
    n,k = map(int, input().split())
    l1 = list(map(int, input().split()))
    ans = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append((l1[i],i))
    l.sort(key = lambda x:x[0])
    ans.sort()
    lo = [-1]*n
    for i in range(n):
        lo[l[i][1]] = ans[i]
    print(*lo)
    
for _ in range((int(input()))):
    solve()
