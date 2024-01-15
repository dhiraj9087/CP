from collections import Counter
import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(1)
        return
    a.sort()
    # print(a)
    q=0
    for i in range(n-1):
        q=math.gcd(q,a[i+1]-a[i])
    # print(q)
    ans=0
    for i in range(n):
        ans+=((a[n-1]-a[i])//q)
    # print(ans)
    d=Counter(a)
    val=0
    flag=False
    for i in range(a[n-1],a[0]-1,-q):
        if i not in d:
            val=i
            flag=True
            break
    if flag==True:
        ans+=(a[n-1]-val)//q
        print(ans)
        return
    print(ans+n)
    

    # y=a[n-1]-q
    # ans=0
    # ans2=0
    # if y not in a:
    #     a.append(y)
    #     for i in range(n+1):
    #         ans+=(abs(y)-abs(a[i]))
    # # for i in range(n):
    # #     ans+=(abs(x)-abs(a[i]))
    #     # ans2+=(abs(y)-abs(a[i]))
    # print(ans,ans2)
    # print(math.gcd(*a))
for _ in range(int(input())):
   main()