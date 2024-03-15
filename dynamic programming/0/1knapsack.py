n=4
a=[1,2,4,5]
b=[5,4,8,6]
w=5
dp=[[0 for i in range(w+1)] for j in range(n)]
for i in range(a[0],w+1):
    dp[0][i]=b[0]
# if a[0]<=w:
#     dp[0][a[0]]=1
for i in range(1,n):
    for j in range(1,w+1):
        nottake = 0 + dp[i-1][j]
        take=float('-inf')
        if a[i]<=j:
            take=b[i] + dp[i-1][j-a[i]]
        dp[i][j]=max(take,nottake)
print(dp[n-1][w])




# def knap(ind,wt):
#     if ind==0:
#         if a[0]<=wt: return b[0]
#         else: return 0
#     if dp[ind][wt]!=-1:
#         return dp[ind][wt]
#     nottake = 0+knap(ind-1,wt)
#     take = float('-inf')
#     if a[ind]<=wt:
#         take=b[ind]+knap(ind-1,wt-a[ind])
#     dp[ind][wt]=max(take,nottake)
#     return dp[ind][wt]


# print(knap(n-1,w))





