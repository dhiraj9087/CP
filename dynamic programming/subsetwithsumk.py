# tar=5
# ans=0
# n=4
# arr=[1,4,4,5]
# dp=[[0 for i in range(tar+1)]for j in range(n)]
# for i in range(n):
#     dp[i][0]=1
# if arr[0]<=tar:
#     dp[0][arr[0]]=1
# for i in range(1,n):
#     for j in range(1,tar+1):
#         nottake=dp[i-1][j]
#         take=0
#         if j>=arr[i]:
#             take=dp[i-1][j-arr[i]]
#         dp[i][j]=take+nottake
# print(dp[n-1][tar])

# # def fun(ind,s):
# #     if s==0 :
# #         return 1
# #     if ind==0:
# #         return 1 if (arr[0]==s) else 0
# #     if dp[ind][s]!=-1:
# #         return dp[ind][s]
# #     nottake=fun(ind-1,s)
# #     take=0
# #     if s>=arr[ind]:
# #         take+=fun(ind-1,(s-arr[ind]))
# #     dp[ind][s]=take + nottake
# #     return dp[ind][s]

# # print(fun(n-1,5))
