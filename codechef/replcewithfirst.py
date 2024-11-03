import sys
from collections import Counter

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    s=input().strip()
    t=input().strip()
    l,r=0,0
    ans = 0
    while l<n and r<m:
        if s[l]==t[r]:
            l+=1
            r+=1
        else:
            while r<m and s[l]!=t[r]:
                r+=1
                ans+=1
    print(ans)
for _ in range(int(input())):
    main()
