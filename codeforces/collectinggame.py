import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    a2=sorted(a)
    d=[]
    for i in range(n):
        d.append([a2[i],i])
    print(d)
    for i in range(n):
        ans.append([])
for _ in range(int(input())):
   main()