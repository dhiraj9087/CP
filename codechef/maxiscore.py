import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print(0)
        return
    maxi=max(a)
    arr=[maxi-a[i] for i in range(n)]
    l=0
    if m==1:
        print(sum(arr))
        return
    if m*arr[0]>sum(arr):
        print(a[0])
        return
    print(math.ceil(sum(arr)/m))
    

    # while len(set(arr))==0 and arr[0]==0:
    #     for i in range(l,m):
            
    #         arr[i]-=1

    # print(arr)
for _ in range(int(input())):
   main()