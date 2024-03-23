import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    ind = (n + 1) // 2 - 1
    # print(ind)
    c=0
    for i in range(ind,n):
        if b[i]<=b[ind]:
            c+=1
    print(c)
for _ in range(int(input())):
   main()