import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]==min(a) or a[-1]==min(a):
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
   main()