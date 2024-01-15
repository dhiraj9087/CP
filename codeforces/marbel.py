import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    if a % b == 0:
        print(0)
        return
    ans1,ans2 = 0,0
    x,y = a,b
    flag,flag2=False,False
    while a >= b:
        a -= 1
        b += 1
        ans1 += 1
        if a % b == 0:
            flag = True
            break
    a,b = x,y
    while b > 0:
        a += 1
        b -= 1
        ans2 += 1
        if a % b == 0:
            flag2=True
            break
    if flag == True and flag2 == True:
        print(min(ans2,ans1))
        return
    if flag == True:
        print(ans1)
        return
    print(ans2)
for _ in range(int(input())):
   main()