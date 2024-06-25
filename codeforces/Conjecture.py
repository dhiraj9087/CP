import math
import sys
input=sys.stdin.readline


def main():
    x,y,k=map(int,input().split())
    d=x%y
    d=y-d
    if k<d:
        print(x+k)
        return
    if d==k:
        x+=k
        while x%y==0:
            x//=y
        print(x)
        return
    while True:
        b=d
        if x==1:
            break
        if k>=b:
            k-=b
            x+=b
            while x%y==0:
                x//=y
            d=y - x%y
        else:
            x+=k
            k=0
            break
    if k!=0:
        
        print(k%(y-1)+1)
        return
    
    

    print(x)
    return
for _ in range(int(input())):
   main()