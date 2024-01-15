import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    add=sum(a)
    s=0
    for i in range(n):
        s+=a[i]
        if s>add//2:
            print(i+1)
            return
        
# for _ in range(int(input())):
main()