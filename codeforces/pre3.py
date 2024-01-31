import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(zip(a,b))
    c.sort(key=lambda x:x[0])
    x,y=[],[]
    for i,j in c:
        x.append(i)
        y.append(j)
    print(*x)
    print(*y)
for _ in range(int(input())):
   main()