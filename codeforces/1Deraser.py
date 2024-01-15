import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    s=input()
    ans=ind=0
    while ind<n:
        if s[ind]=='B':
            ans+=1
            ind+=k
        else:
            ind+=1   
    print(ans)
for _ in range(int(input())):
   main()