import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n==1:
        print(1)
        return
    ans=0
    a=1
    while a<=n:
        a*=2
        ans+=1
    print(1<<(ans-1))
for _ in range(int(input())):
   main()