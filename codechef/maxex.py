import math
import sys
input=sys.stdin.readline

def cal(x,n,k):
   return (x%k)*((n-x)%k)

def main():
    n,k=map(int,input().split())
    if n<k:
        if cal(n//2,n,k)>cal((n+1)//2,n,k):
            print(n//2)
            return
        print((n+1)//2)
        # print(max(n//2,(n+1)//2))
        return
    n1=n%k
    if n%k==0:
        n1=k
    n2= k + n%k
    a1,a2,a3,a4=cal(n1//2,n,k),cal((n1+1)//2,n,k),cal(n2//2,n,k),cal((n2+1)//2,n,k)
    # ans=max(n1//2,(n1+1)//2,n2//2,(n2+1)//2)
    # print(n1//2,(n1+1)//2,n2//2,(n2+1)//2)
    if a1>=a2 and a1>=a3 and a1>=a4:
        print(n1//2)
        return
    if a2>=a1 and a2>=a3 and a2>=a4:
        print((n1+1)//2)
        return
    if a3>=a1 and a3>=a2 and a3>=a4:
        print(n2//2)
        return
    if a4>=a1 and a4>=a3 and a4>=a2:
        print((n2+1)//2)
        return

    
    # ans = (n // k) * k + min(k // 2, n % k)
    # print(10**9)
    # for i in range(0,10**9//2,2):
    #    print(i)
    # ans=float('-inf')
    # maxi=float('-inf')
    # # if k%2==0:
    # #     for i in range(1,n+1):
    # #     # ans=max(ans,(i%k)*((n-i)%k))
    # #     # print(ans,(i%k)*((n-i)%k))
    # #         a=(i%k)*((n-i)%k)
    # #         print(a)
    # #         if a>maxi:
    # #             maxi=a
    # #             ans=i
    # #     print(ans,n//2)
    # for i in range(k):
    #     # ans=max(ans,(i%k)*((n-i)%k))
    #     # print(ans,(i%k)*((n-i)%k))
        
    #     if i>n:
    #         break
    #     # a=(i*(n-i))%k
    #     # print(a)
    #     a=(i%k)*((n-i)%k)
    #     if a>maxi:
    #         maxi=a
    #         ans=i
    # print(ans)
    # l,r=0,n
    # while l<=r:
    #     mid = (l+r)//2
    #     a=cal(mid,n,k)
    #     b=cal(mid-1,n,k)
    #     c=cal(mid+1,n,k)
    #     if a>=b and a>=c:
    #         print(mid)
    #         return
    #     elif b>a:
    #         r=mid-1
    #     else:
    #         l=mid+1
for _ in range(int(input())):
   main()