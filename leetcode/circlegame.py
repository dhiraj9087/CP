import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if n%2==1:
        print("Mike")
        return
    ind=a.index(min(a))
    if ind%2==0:
        print("Joe")
        return
    print("Mike")

for _ in range(int(input())):
   main()