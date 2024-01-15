# for i in range((int(input()))):
#     n=int(input())
#     a=list(map(int,input().split()))
#     c=0
#     a.sort()
#     for i in range(n):
#         for j in range(i+1,n):
#             if a[i]<a[j]:
#                 c+=1
#     print(c) 
import math
def ctfinal(n):
    pair = n * (n - 1) // 2
    return pair

def solve():
    n = int(input())
    mp = {}
    a=list(map(int,input().split()))
    for i in range(n):
        # ins = int(input())
        if a[i] in mp:
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1
    ans = ctfinal(n)
    # print(mp,ansm)
    for cmp in mp.values():
        print(cmp)
        pairs = ctfinal(cmp)
        ans -= pairs
    print(ans)

t = int(input())
for _ in range(t):
    solve()


