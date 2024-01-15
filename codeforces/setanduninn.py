import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    full=set()
    a=[set() for i in range(n)]
    # print(a)
    for i in range(n):
        s=list(map(int,input().split()))
        for ele in range(1,len(s)):
        # for ele in s:
        #     # if ele!=s[-1]:
                a[i].add(s[ele])
                full.add(s[ele])
    # for i in range(len(a)):
    #     for j in a[i]:
    #         full.append(j)
    # full=set(full)
    # print(full,a) 
    ans=float('-inf')
    for i in full:
        res=set()
        for j in a:
            if i not in j:
                res = res|j
                # for k in j:
                #     res.add(k)
                # print(res,len(res))
        ans=max(ans,len(res))

    # print(ans,res)
    print(ans)
    
for _ in range(int(input())):
   main()