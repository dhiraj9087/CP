import math
import sys
input=sys.stdin.readline
def main():
    n,l=map(int,input().split())
    if l*2 >= n*(n+1):
        a=[]
        for i in range(1,n+1):
            print(i,end=' ')
        # print(*a)
        print()
        return
    ind=1
    ans=[]
    while ind<=n and ind*(ind+1)<=2*l:
        print(ind,end=' ')
        ind+=1
    ind-=1
    rem = n-ind
    temp=ind
    while rem>0:
        add = temp+l
        print(add,end=' ')
        temp = add
        rem-=1
    print()
    # print(*ans)
for _ in range(int(input())):
   main()