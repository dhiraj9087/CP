import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    add=sum(a)
    if len(set(a))==1:
        print("Yes")
        return
    if add%n!=0:
        print("No")
        return
    can=add//n
    for i in range(n):
        if abs(a[i]-can)%2!=0:
            print("No")
            return
    print("Yes")

for _ in range(int(input())):
   main()