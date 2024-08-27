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

def optimize_power(a, b, c):
    x = -(-a // 100)  # Ceiling division
    y = 0
    min_power = b * x

    while x > 0:
        new_x = x - 1
        new_y = -(-max(0, a - 100 * new_x) // 4)  # Ceiling division
        new_power = b * new_x + c * new_y

        if new_power < min_power:
            x, y = new_x, new_y
            min_power = new_power
        else:
            break

    return x, y, min_power

# Example usage:
a = 1000  # number of customers
b = 500   # power consumption of engine m
c = 30    # power consumption of engine n

x, y, min_power = optimize_power(a, b, c)
print(f"Use {x} m engines and {y} n engines")
print(f"Minimum power consumption: {min_power}")