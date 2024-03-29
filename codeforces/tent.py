import math
import sys
input=sys.stdin.readline
def main():
    i,e,u=map(int,input().split())
    ans=0
    ans=i
    if e%3==0:
        ans+=3
    if e>0 and u>0 and e%3 + u <=2 :
        print(-1)
        return
    print((ans+(e+u+2)//3))
for _ in range(int(input())):
   main()