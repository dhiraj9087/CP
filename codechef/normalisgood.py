import math
import sys
input=sys.stdin.readline
def mean(a):
    return sum(a)/len(a)
def median(a):
    a.sort()
    if len(a)%2==1:
        return a[len(a)//2]
    return a[len(a)//2 - 1]

def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i,n):
            sub = a[i:j+1]
            a1 = mean(sub)
            a2 = median(sub)
            # print(sub,a1,a2)
            if a1 == a2:
                ans+=1
    print(ans)
for _ in range(int(input())):
   main()