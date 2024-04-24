import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    # for i in range(n):
    #     print(a[i]%k,end=' ')
    # print()
    # print(max(a)-min(a))
    if k==1:
        print(0)
        return
    
    # l1,l2=[],[]
    # mini=min(a)
    # maxi=max(a)
    # a.sort()
    # mod = a[-1]%k
    # ind=-1
    # for i in range(n):
    #     if a[i]-mini > maxi-a[i]:
    #         ind=i
    #         break
    # print(ind)
    # arr=a.copy()
    # for i in range(ind):
    #     arr[i]+=(k*mod)
    # print(arr,max(arr)-min(arr))   
    a.sort()
    maxi = a[-1]
    for i in range(n - 1):
        tmp = (maxi - a[i]) // k
        a[i] += tmp * k
    # print(a)
    mini = min(a)
    # for i in range(n):
    #     mini = min(mini, a[i])
    ans = maxi - mini
    a.sort()
    maxi = a[-1]
    for i in range(n):
        ans = min(ans, maxi - a[i])
        maxi = max(maxi, a[i] + k)
    print(ans)
    
for _ in range(int(input())):
   main()