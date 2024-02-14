import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if n > 3:
        print("YES")
        return
    if n == 1:
        print("YES")
        return
    if n == 2:
        if a[0] > a[1]:
            print("NO")
        else:
            print("YES")
        return
    if n == 3:
        if a[0] <= a[1] <= a[2]:
            print("YES")
        elif a[2] <= a[1] <= a[0]:
            print("YES")
        else:
            print("NO")

for _ in range(int(input())):
   main()