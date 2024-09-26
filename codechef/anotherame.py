import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if sorted(a)==a:
        print(0)
        return
    # b = sorted(a)
    # arr=[]
    # for i in range(n):
    #     if a[i]!=b[i]:
    #         arr.append(a[i])
    # # print(arr)
    # # print(max(arr)+min(arr))
    # ans=0
    # for i in range(1,n):
    #     ans = max(ans,b[i]+b[i-1])
    # print(ans)
    b=a[:]
    a.sort()
    ans=0
    for i in range(n-1,-1,-1):
        if a[i]!=b[i]:
            ans = 1+max(a[i],b[i])
            break
    print(ans)

for _ in range(int(input())):
   main()


  