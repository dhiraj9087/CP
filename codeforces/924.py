import math
import sys
input=sys.stdin.readline
def main():
    x,y=map(int,input().split())
    if (x%2!=0 and y%2!=0) or (x%2!=0 and y//2==x) or (y%2!=0 and x//2==y) or (x==1 and y==1):
        print("No")
        return
    print("Yes")

for _ in range(int(input())):
   main()