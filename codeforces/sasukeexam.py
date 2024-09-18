import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    if a%2==1:
        print("NO")
        return
    if a==0 and b%2==1:
        print("NO")
        return
    print("YES")
for _ in range(int(input())):
   main()