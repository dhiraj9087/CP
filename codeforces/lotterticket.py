import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    chef = a[0]
    a.sort()
    if chef==a[0]:
        # print((a[1]-a[0]+1)//2 + chef)
        if (a[1]-a[0])%2==1:
            print((a[1]-a[0]+1)//2 + chef)
            return
        print((a[1]-a[0]+1)//2 + chef-1)
    if chef==a[-1]:
        if (a[-1]-a[-2])%2==1:
            print((a[-1]-a[-2]+1)//2 + 1000000-chef)
            return
        print((a[-1]-a[-2]+1)//2 + 1000000-chef-1)
    prev,next=0,0
    for i in range(1,n-1):
        if chef==a[i]:
            prev=a[i-1]
            next=a[i+1]
            break
    print(((chef-prev)//2)+((next-chef)//2)+1)
for _ in range(int(input())):
   main()
print(3%3)