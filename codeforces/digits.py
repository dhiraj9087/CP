import math
import sys
input=sys.stdin.readline

def is3(n,d,ans):
    if n==1:
        if d%3==0:
            ans.append(3)
    elif n==2:
        if (d*2)%3==0:
            ans.append(3)
    else:
        ans.append(3)
def is7(n,d,ans):
    if n<=6:
        f=math.factorial(n)
        s=str(d)*(f)
        if int(s)%7==0:
            ans.append(7)
    else:
        ans.append(7)
def is9(n,d,ans,d3):
    if n<8:
        if (d*(d3[n]))%9==0:
            ans.append(9)
    else:
        ans.append(9)
def main():
    n,d=map(int,input().split())
    #1,3,5,7,9
    ans=[1]
    is3(n,d,ans)
    if d%5==0:
        ans.append(5)
    is7(n,d,ans)
    d3={1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320}

    is9(n,d,ans,d3)

    print(*ans)
    # print(math.factorial(8)/9)
for _ in range(int(input())):
   main()