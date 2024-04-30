import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a=[0]+a
    flag=False
    for i in range(1,n):
        if i==a[a[i]]:
            flag=True
            break
    if flag==True:
        print(2)
        return
    print(3)
for _ in range(int(input())):
   main()