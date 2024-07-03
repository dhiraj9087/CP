import math
import sys
input=sys.stdin.readline

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    rem_a,rem_b = [0]*m,[0]*m
    for i in a:
        rem = i%m
        rem_a[rem] += 1
    for i in b:
        rem = i%m
        rem_b[rem] += 1
    ans=0
    # print(rem_a,rem_b)
    for i in range(m):
        if i==0:
            ans+=(rem_a[i]*rem_b[i])
        else:
            ans+=(rem_a[i] * rem_b[m-i])
    print(ans)
        
for _ in range(int(input())):
   main()