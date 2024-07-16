import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    if n==1:
        print(0)
        return
    rem=n
    ans=0
    while True:
        rem -= (k-1)
        ans+=1
        if rem<=1:
            break
    print(ans)
for _ in range(int(input())):
   main()