import math
import sys
input=sys.stdin.readline
mod=1e+7
def main():
    n,k=map(int,input().split())
    # # if math.ceil(math.log2(n))!=math.floor(math.log2(n)):
    # #     print('-1')
    # #     return
    # if (n == 0 or (n & (n - 1)) != 0) and k%2==0:
    #     print('-1')
    #     return
    # if n>k:
    #     print('-1')
    #     return
    # # if k%n==0:
    # #     ans=[k//n]*(n)
    # #     for i in range(n//2-1):
    # #         ans[i]+=1
    # #         ans[i+1]-=1
    # #     print(*ans)
    # #     return
    # # else:
    # #     ans=[k//n]*(n)
    # #     rem=k%n
    # #     # print(ans,rem)
    # #     for i in range(k%n):
    # #         ans[i]+=1
    # #     print(*ans)
    # ans=[0]*n
    # ans[0]=10**5 - (k-n)
    # ans[-1]=2
    # for i in range(n):
    #     if ans[i]==0:
    #         ans[i]=1
    # odd,even=0,0
    
    # # print(ans,even,odd)
    # l=0
    # r=n-2
    # add=sum(ans)
    # # print(add)
    # if even==odd:
    #     print(*ans)
    #     return
    # if abs(even-odd)%2!=0:
    #     print('-1')
    #     return
    # # if ans[0]%2!=0:
    # ans[0]-=abs(even-odd)//2
    # for i in range(1,(abs(even-odd)//2)+1):
    #     ans[i]+=1
    # print(*ans)
    # # if ans[0]%2==0:

    # # while even!=odd:
    # #     if ans[0]%2==0:
    # #         ans[r]+=1
    # #         ans[l]-=1
    # #         even+=1
    ans=[0]*n
    add=k
    for i in range(0, n, 2):
        ans[i] = 1
    for i in range(1, n, 2):
        ans[i] = 2
    k = k-sum(ans)
    # print(k)
    if k<0:
        print('-1')
        return
    # if (n == 0 or (n & (n - 1)) != 0) and k%2==0:
    #     print('-1')
    #     return
    for i in range(n):
        diff = 10**5 - ans[i]
        if diff % 2 != 0:
            diff -= 1
        can = k
        if can % 2 != 0:
            can -= 1
        mini = min(can, diff)
        ans[i] += mini
        k -= mini
    flag=False
    # if len(ans)!=n or sum(ans)!=k:
    #     flag=True
    odd,even=0,0
    for i in ans:
        if i%2==0:
            even+=1
        else:
            odd+=1
        if 1<=i<=10**5:
            continue
        flag=True
    if len(ans)!=n or sum(ans)!=add or odd!=even:
        print('-1')
        return
    print(*ans)
for _ in range(int(input())):
   main()