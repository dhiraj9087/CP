import math
import sys
input=sys.stdin.readline
import bisect

def main():
    n,m,q=map(int,input().split())
    t=[]
    t=list(map(int,input().split()))
    t.sort()
    arr = list(map(int,input().split()))
    for i in range(q):
        x=arr[i]
        if x<t[0]:
            print(t[0]-1)
        elif x>t[m-1]:
            print(n-t[m-1])
        else:
            b = bisect.bisect_left(t,x)
            print((t[b]-t[b-1])//2)
            
        
for _ in range(int(input())):
   main()