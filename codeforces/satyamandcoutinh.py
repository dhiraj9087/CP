import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    zero=[]
    one=[]
    d1,d2={},{}
    ans=0
    for i in range(n):
        x,y=map(int,input().split())
        if y==0:
            zero.append(x)
            d1[x] = d1.get(x,0)+1
        else:
            one.append(x)
            d2[x] = d2.get(x,0)+1
    for i in one:
        if i in d1:
            ans += len(zero) -1 + len(one) -1
    for i in one:
        if (i+1) in d1 and (i-1) in d1:
            ans+=1
    for i in zero:
        if (i+1) in d2 and (i-1) in d2:
            ans+=1
    print(ans)            

for _ in range(int(input())):
   main()