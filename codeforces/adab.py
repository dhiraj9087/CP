import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    if a==b:
        print('01'*a)
        return
    maxi=-1
    if a>b:
        maxi='0'
    else:
        maxi='1'
    d=abs(a-b)
    ans=""
    ans='01'*(min(a,b))
    # ans+='1'*(min(a,b))
    ans+=maxi*(d)
    print(ans)
for _ in range(int(input())):
   main()