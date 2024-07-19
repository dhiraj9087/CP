import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n==1:
        print(1)
        print(1)
        return
    ans=[]
    num=0
    for i in range(1,n+1):
        if not (i&(i-1)):
            num+=1
        ans.append(num)
    print(num)
    print(*ans)
    # print(num,*ans)
for _ in range(int(input())):
   main()