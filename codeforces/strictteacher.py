import math
import sys
input=sys.stdin.readline
def main():
    n,m,q=map(int,input().split())
    t1,t2=map(int,input().split())
    q=int(input())
    if q==1 or q==n:
        print(min(abs(t1-q),abs(t2-q)))
        return
    if t1<=q<=t2 or t2<=q<=t1:
        print(((max(t1,t2)-min(t1,t2)))//2)
        return
    if q>t1 and q>t2:
        # stu = n-q
        # te = min(q-t1,q-t2)
        print(n-max(t1,t2))
        return
    # stu = q-1
    # te = min(t1-q,t2-q)
    print(min(t1,t2)-1)
    
for _ in range(int(input())):
   main()