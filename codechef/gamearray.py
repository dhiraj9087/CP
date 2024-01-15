import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    if n==1 and a[0]>=2:
        print("Alice")
        return
    if s%2!=0:
        print("Bob")
        return
    x=0
    for i in range(n):
        if i%2==0:
            x+=a[i]
    if x%2!=(s//2)%2:
        print("Alice")
        return
    print("Bob")
for _ in range(int(input())):
   main()