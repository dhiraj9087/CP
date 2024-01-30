import math
import sys
input=sys.stdin.readline
def main():
    x, n = map(int, input().split())
    if n==x:
        print(1)
        return
    if n==1:
        print(x)
        return
    ans=1
    for i in range(1, x//n +1):
        if x%i==0:
            if x//i >= n:
                ans=i
            else:
                break
    print(ans)
for _ in range(int(input())):
   main()