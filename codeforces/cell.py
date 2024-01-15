import math
import sys
input=sys.stdin.readline
def main():
    a,b,c=map(int,input().split())
    if a==b==c:
        print(1,1,1)
        return
    if max(a,b,c)==a:
        print(1,0,0)
        return
    if max(a,b,c)==b:
        print(0,1,0)
        return
    print(0,0,1)
for _ in range(int(input())):
   main()