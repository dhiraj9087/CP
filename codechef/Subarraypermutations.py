def solve():
    n,k=map(int,input().split())
    if n==1 and k==1:
        print(1)
        return
    if k<2:
        print(-1)
        return
    
    # p=[i for i in range(1,n+1)]
    # a=[i for i in range(1,k)]
    # for i in range(n-1,k+1,-1):
    #     a.append(p[i])
    # print(*a)
    
    for i in range(1,k):
        print(i,end=' ')
    for i in range(k+1,n+1):
        print(i,end=' ')
    print(k)

for _ in range((int(input()))):
    solve()
 

# n, k = map(int, input().split())
#     if n == 1 and k == 1:
#         print(1)
#         return
#     if k < 2:
#         print(-1)
#         return
#     for i in range(1, k):
#         print(i, end=" ")
#     for i in range(k + 1, n + 1):
#         print(i, end=" ")
#     print(k)