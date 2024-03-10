# arr=[3, 1, 1, 2, 2, 1]
# s=sum(arr)
# k=s//2
# n=len(arr)
# dp=[[False for j in range(k+1)] for i in range(n)]
# for i in range(n):
#     dp[i][0]=True
# if arr[0]<=k:
#     dp[0][k]==True
# for i in range(1,n):
#     for j in range(1,k):
#         nottake=dp[i-1][j]
#         take=False
#         if arr[i]<=j:
#             take=dp[i-1][j-arr[i]]
#         dp[i][j]=(take or nottake)
# print(dp[n-1][j])
# # def sub(ind,k):
# #     if k==0:
# #         return True
# #     if ind==0:
# #         if arr[0]==k:
# #             return True
# #         return False
# #     if dp[ind][k]!=-1:
# #         return dp[ind][k]
# #     nottake =  sub(ind-1,k)
# #     take=False
# #     if arr[ind]<=k:
# #         take = sub(ind-1,k-arr[ind])
# #     dp[ind][k]=(take or nottake)
# #     return dp[ind][k]
# # print(sub(n-1,k))