import math
import sys
input=sys.stdin.readline
def main():
    r,g,b=map(int,input().split())
    if r<=g+b and g<=r+b and b<=r+g:
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
   main()