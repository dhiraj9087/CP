import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    n=int(input())
    a=list(map(int,input().split()))
    
    d=Counter(a)
    for i,j in d.items():
        if j%2==1:
            print("YES")
            return
    print("NO")
for _ in range(int(input())):
   main()