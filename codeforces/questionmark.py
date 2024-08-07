import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    a,b,c,d=s.count('A'),s.count('B'),s.count('C'),s.count('D')
    ans=0
    if a>=n:
        ans+=n
    else:
        ans+=a
    if b>=n:
        ans+=n
    else:
        ans+=b
    if c>=n:
        ans+=n
    else:
        ans+=c
    if d>=n:
        ans+=n
    else:ans+=d
    print(ans)
for _ in range(int(input())):
   main()