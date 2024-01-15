import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n<7 or n==9:
        print("NO")
        return
    if n%3==0:
        print("YES")
        print(1,4,n-5)
        return
    if n%3!=0:
        print("YES")
        print(1,2,n-3)
        return
    
    print("NO")
for _ in range(int(input())):
   main()