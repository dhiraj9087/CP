import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    even,odd=0,0
    if len(a)==1:
        if a[0]<=0:
            print(0)
            return
        print(a[0])
        return
    for i in range(2,n):
        if a[i]>0:
            odd+=a[i]
    if a[1]<0:
        a[1]=0
    if (a[0]+a[1])>0:
        odd+=a[0]+a[1]
    print(odd)
for _ in range(int(input())):
   main()