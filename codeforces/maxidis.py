import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n==1:
        print(1)
        print(1)
        return
    if n==2:
        print(1,2)
        print(2,1)
        return
    a,b=[],[]
    if n%2==0:
        for i in range(1,n+1):
            a.append(i)
        for i in range(n//2+1,n+1):
            b.append(i)
        for i in range(1,n//2+1):
            b.append(i)
        print(*a)
        print(*b)
        return
    for i in range(1,n+1):
        a.append(i)
    for i in range(n//2+2,n+1):
        b.append(i)
    for i in range(1,n//2+2):
        b.append(i)
    print(*a)
    print(*b)
for _ in range(int(input())):
   main()