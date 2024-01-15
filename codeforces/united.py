from collections import defaultdict
import math
import sys
input=sys.stdin.readline


def main():
    a,b,c=map(int,input().split())
    if c%2==0:
        if a>b:
            print("First")
            return
        print("Second")
    else:
        if b>a:
            print("Second")
            return
        print("First")
    
for _ in range(int(input())):
    main()



