import math
import sys
input=sys.stdin.readline
def main():
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    i=0
    while i<n:
        if r>=(i+1):
            if a[i]<=2:
                ans+=a[i]
                i+=1
            else:
                ans+=2
                i+=2
    # for i in range(n):
    #     if r>=(i+1):   
    #         if a[i]<=2:
    #             ans+=a[i]
    #         else:
    #             ans+=2
    #             i+=1
    print(ans)
            
for _ in range(int(input())):
   main()