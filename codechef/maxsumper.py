# def solve():
#     n,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     # ev,od=[],[]
#     # for i in range(n):
#     #     if a[i]%2==0:
#     #         ev.append(a[i])
#     #     else:
#     #         od.append(a[i])
#     # print(ev,od)
#     # q=[*ev]
#     # od.sort(reverse=True)
#     # for i in range(len(od)):
#     #     q.append(od[i])
#     # print(q)  
#     # a.sort(reverse=True)
#     # q=[*a]
#     q=[0]*n
    
#     ps=[0]
#     e=0
#     for i in range(len(q)):
#         e+=q[i]
#         ps.append(e)
#     # print(ps)
#     x=0
#     for i in range(k):
#         l,r=map(int,input().split())
#         x=x+ps[r]-ps[l-1]
#     print(x)
#     print(*q)
# for _  in range((int(input()))):
#     solve()

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = [int(i) for i in input().split()]
    diff = [0 for i in range(n)]
    
    for i in range(q):
        l, r = map(int, input().split())
        diff[l-1] += 1 
        if r < n:
            diff[r] -= 1 
    print(diff)
    for i in range(1, n):
        diff[i] += diff[i-1]
    print(diff)
    temp = []
    for i in range(n):
        temp.append([diff[i], i])
    temp.sort()
    arr.sort()
    print(temp)

    total = 0 
    for i in range(n):
        total += arr[i]*temp[i][0]
        temp[i][0] = arr[i]
    print(temp)
    temp.sort(key=lambda x: x[1])
    print(temp)
    ans = []
    for i in range(n):
        ans.append(temp[i][0])
    
    print(total)
    print(*ans)
    
    
    