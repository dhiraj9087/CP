import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[a[i]*b[i] for i in range(n)]
    maxi=max(c)
    ans=[]
    for i in range(n):
        if c[i]==maxi:
            ans.append(b[i])
    maxi2=max(ans)
    for i in range(n):
        if b[i]==maxi2:
            print(i+1)
            return

for _ in range(int(input())):
   main()