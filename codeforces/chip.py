import math
import sys
input=sys.stdin.readline
def main():
    h,w,xa,ya,xb,yb=map(int,input().split())
    if abs(xa-xb)%2==1:
        print("Alice,Draw",abs(ya-yb),abs(abs(xa-xb)-abs(ya-yb)),abs(xa-ya))
        return
    print("Bob,Draw",abs(ya-yb),abs(abs(xa-xb)-abs(ya-yb)))
    print("Yes ")
for _ in range(int(input())):
   main()