import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    odd,even=0,0
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1
    if k==0 and odd==n:
        ans=1
        for i in range(2,n+1):
            ans*=i
        print(ans)
        return
    

for _ in range(int(input())):
   main()