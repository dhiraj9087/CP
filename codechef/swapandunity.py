import math
import sys
input=sys.stdin.readline
from collections import Counter
def is_alternating_string(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True
def main():
    s=input().strip()
    n=len(s)
    d=Counter(s)
    res=float('inf')
    for i,j in d.items():
        l,r=0,j-1
        extra = len(s[l:r+1])-s[l:r+1].count(i)
        ans=extra
        while r<=n-1:
            ans=min(ans,extra)
            if s[l]!=i:
                extra-=1
            l+=1
            r+=1
            if r<=n-1 and s[r]!=i:
                extra+=1
        res=min(res,ans)
    print(res)
    # for i in range(len(s)):
    #     if s[i] not in d:
    #         d[s[i]]=[i]
    #     else:
    #         d[s[i]].append(i)
    # for i,j in d.items():
    #     if j==1:
    #         print(0)
    #         return
    # if is_alternating_string(s):
    #     print(1)
    #     return
    # same = {}
    # curr = s[0]
    # count = 1
    # for i in range(1, len(s)):
    #     if s[i] == curr:
    #         count += 1
    #     else:
    #         same[curr] = count
    #         curr = s[i]
    #         count = 1
    # same[curr] = count
    # print(d,same)
    # ans=float('inf')
    # for i in s:
    #     ans=min(ans,abs(d[i]-same[i]))
    # print(ans)
    # d2={i:0 for i in s}
    # for i in range(n-1):
    #     if s[i]==s[i+1]:
    #         d2[s[i]]+=1
    # same=set()
    # for i,j in d.items():
    #     same.add(j)
    #     if len(same)>1:
    #         break
    # if len(same)==1 and next(iter(d.values()))==n//2:
    #     print(1)
    #     return
    
    # ans=float('inf')
    # print(min(d2.values()))
    # print(d,d2)
for _ in range(int(input())):
   main()