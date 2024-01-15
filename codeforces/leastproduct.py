from collections import Counter
import math
import sys
input=sys.stdin.readline
def main():
    # n=int(input())
    a=list(map(int,input().split()))
    d=Counter(a)
    for i,j in d.items():
        if j==1:
            print(i)
            return
        
for _ in range(int(input())):
    main()