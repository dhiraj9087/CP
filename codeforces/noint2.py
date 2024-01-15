import math
import sys
input=sys.stdin.readline
def main():
    n, k, x = map(int, input().split())
    a =list(map(int, input().split()))
    a.sort(reverse=True)
    # arr=[0]*(n+1)
    for i in range(1,n):
        a[i]+=a[i-1]
        # arr[i]=arr[i-1]+a[i-1]
    a=[0]+a
    ans=float('-inf')
    for i in range(k+1):
        ans=max(ans,a[n] - 2 * a[min(i + x, n)] + a[i])
    print(ans)
for _ in range(int(input())):
   main()
