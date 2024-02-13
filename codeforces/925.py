import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n<=28:
        print('aa'+chr(96+n-2))
        return
    elif n<=53:
        n-=26
        print('a'+chr(96+n-1)+'z')
        return
    else:
        n-=52
        print(chr(96+n)+"zz")
        return
for _ in range(int(input())):
   main()