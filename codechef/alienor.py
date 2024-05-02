import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    arr=[]
    ind=[0]*(k)
    for i in range(n):
        s=input().strip()
        arr.append(s)
        if s.count('1')==1:
            ind[s.index('1')]=1
    if all(ind)==1:
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
   main()