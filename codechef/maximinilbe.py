import math
import sys
input=sys.stdin.readline
def count_special_subsets(n, arr):
    count = [0] * (n + 2)  # Count array to store frequency of differences
    result = 0

    for num in arr:
        if 1 <= num <= n:
            count[num] += 1
    
    for i in range(1, n + 1):
        if count[i] > 0:
            result += count[i] * count[i + 1]
    
    return result

def powerset(nums,ans):
    c=0
    for i in range(1<<len(nums)):
        l=[]
        for j in range(len(nums)):
            if i & (1<<j):
                l.append(nums[j])
        ans.append(l)

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if a[j]-a[i] == j-i+1:
                ans+=1
    print(ans)
for _ in range(int(input())):
   main()




# tar=5
#     ans=0
#     n=4
#     arr=[1,4,4,5]
#     dp=[[0 for i in range(tar+1)]for j in range(n)]
#     for i in range(n):
#         dp[i][0]=1
#     if arr[0]<=tar:
#         dp[0][arr[0]]=1
#     for i in range(1,n):
#         for j in range(1,tar+1):
#             nottake=dp[i-1][j]
#             take=0
#             if j>=arr[i]:
#                 take=dp[i-1][j-arr[i]]
#             dp[i][j]=take+nottake
#     print(dp[n-1][tar])

    # def fun(ind,s):
    #     if s==0 :
    #         return 1
    #     if ind==0:
    #         return 1 if (arr[0]==s) else 0
    #     if dp[ind][s]!=-1:
    #         return dp[ind][s]
    #     nottake=fun(ind-1,s)
    #     take=0
    #     if s>=arr[ind]:
    #         take+=fun(ind-1,(s-arr[ind]))
    #     dp[ind][s]=take + nottake
    #     return dp[ind][s]
    # print(fun(n-1,5))
