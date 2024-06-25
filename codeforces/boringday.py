import math
import sys
input=sys.stdin.readline

def main():
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    add=0
    ind=0
    for i in range(n):
        add+=a[i]
        while add > r and ind <= i:
                add -= a[ind]
                ind += 1
        if l<=add<=r:
            ans+=1
            add=0
            ind=i+1
    print(ans)
for _ in range(int(input())):
    main()