import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    d = {}
    maxi = max(a)
    ans=[]
    for i in a:
        if d.get(i, 0) == 0:
            ans.append(i)
            d[i] = 1
        else:
            ans.append(maxi)
    print(*ans)
for _ in range(int(input())):
   main()
  