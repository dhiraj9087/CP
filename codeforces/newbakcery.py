import math
import sys
input=sys.stdin.readline
def main():
    n,a,b=map(int,input().split())
    if a>=b:
        print(n*a)
        return
    if a < b-n + 1:
        add = b*(b+1)//2 
        add2 = b-n
        add3 = add2*(add2+1)//2
        add = add - add3
        print(add)
        return
    add = b*(b+1)//2
    add2 = a*(a+1)//2
    add3 = add - add2
    diff = b-a
    print(add3 + (n-diff)*a)
for _ in range(int(input())):
   main()