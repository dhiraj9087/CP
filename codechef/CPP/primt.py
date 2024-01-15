import math
import sys
input=sys.stdin.readline
def main():
    l,r,p=map(int,input().split())
    a=[i for i in range(l,r+1)]
    ans=0
    for i in range(len(a)):
        if a[i]%p==0:
            ans+=(a[i]//p)
    print('First' if ans%2==1 else 'Second')
    
for _ in range(int(input())):
   main()