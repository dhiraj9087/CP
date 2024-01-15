import math
import sys
input=sys.stdin.readline
def main():
    a,b,c=map(int,input().split())
    x=math.gcd(a,math.gcd(b,c))
    s=(a+b+c)//x -3 
    if s<=3:
        print("YES")
        return
    print("NO")

    
for _ in range(int(input())):
   main()