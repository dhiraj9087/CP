import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    x=list(map(int,input().split()))
    p=list(map(int,input().split()))
    l1,l2,r1,r2=0,n-1,n-1,0
    for i in range(n-1):
        if x[i] + p[i] >= x[i+1]:
            l1 = i+1
        else:
            break
    for i in range(n-1,-1,-1):
        if x[i] - p[i] <= x[i-1]:
            r1 = i-1
        else:
            break
    for i in range(n-1,-1,-1):
        if x[i] - p[i-1] <= x[i-1]:
            l2 = i-1
        else:
            break
    for i in range(n-1):
        if x[i] + p[i+1] >= x[i+1]:
            r2 = i+1
        else:
            break   
    if max(l1,r2) + 1 >= min(l2,r1):
        print("YES")
        return
    print("NO") 
    # print(l1,l2,r1,r2,max(l1,r2),min(l2,r1))
for _ in range(int(input())):
   main()