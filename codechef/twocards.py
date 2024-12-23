import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    arr=sorted(zip(A,B))
    # print(arr)
    a,b=arr[-1]
    flag=False
    for i in range(n-1):
        c,d=arr[i]
        if max(a,b)<max(c,d):
            flag=True
            break
    if max(a,b)>max(c,d):
        flag=True
    if flag:
        print("Yes")
        return
    print("No")
    # maxia,maxib=0,0
    # inda,indb=-1,-1
    # for i in range(n):
    #     if b[i]>maxib:
    #         maxib=b[i]
    #         indb=i
    #     if a[i]>maxia:
    #         maxia=a[i]
    #         inda=i
    # if maxib>maxia:
    #     print
for _ in range(int(input())):
   main()