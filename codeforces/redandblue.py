import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    a=list(map(int,input().split()))
    ans=0
    ind=-1
    ind2=-1
    for i in range(n):
        if i>ind and s[i]=='B':
            if i>ind2:
                print(-1)
                return
            ans += 1
            ind = ind2
        ind2 = max(ind2,i+a[i])
    print(ans)
for _ in range(int(input())):
   main()