import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    n-=1
    if n==0:
        print(0)
        return
    a=[]*100
    c=0
    while n:
        c+=1
        a[c]=n%5
        n//=5
    for i in range(c,0,-1):
        print(a[i]*2,end='')
# for _ in range(int(input())):
main()