
import sys
input=sys.stdin.readline
import math

def main():
    n=int(input())
    a=list(map(int,input().split()))
    # # mp=Counter(a)
    # # print(mp)
    # dp=[0]*n
    # mp={}
    # for i in a:
    #     mp[i] = mp.get(i,0) + 1
    # # print(mp)

    # for x in mp:
    #     for i in range(x-1,n,x):
    #         dp[i] += mp[x]
    # print(max(dp))
    mp=[0]*(n+1)
    cnt=[0]*(n+1)
    for x in a:
        if x<=n:
            cnt[x]+=1
    # print(cnt) 
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            mp[j]+=cnt[i]
    print(max(mp))



for _ in range(int(input())):
    main()


#     # n = rint()
#     # dp = [0] * n
#     # arr = rarr()
 
#     # mp = Counter(arr)
 
#     # for x in mp:
#     #     for i in range(x - 1, n, x):
#     #         dp[i] += mp[x]
 
#     # ans = 0
#     # for i in range(n):
#     #     ans = max(ans, dp[i])
 
#     # print(ans)
# t= int(input())
# for ir in range(t):
#     n=int(input())
#     a, cnt= [0]*(n+1), [0]*(n+1)
#     for x in list(map(int, input().split())):
#         if x <= n: cnt[x]+=1
#     for x in range(1, n+1):
#         for y in range(x, n+1, x): a[y]+= cnt[x]
#     print(max(a))
