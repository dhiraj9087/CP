import math
import sys
input=sys.stdin.readline
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    arr = a.copy()
    arr.sort()
    ans=0
    l, r = 0, 2**31-1
    while l <= r:
        mid = l + (r - l) // 2
        res=0
        for i in a:
            if mid>i:
                res+=(mid-i)
                
        if res<=k:
            ans=mid
            l=mid+1
        else:
            r=mid-1

    print(ans)


    



for _ in range(int(input())):
   main()