arr = [1,3,5]
# arr = [2,4,6]

# arr=[1,2,3,4,5,6,7]
n=len(arr)
# pre=[0]*(n)
mod=10**9+7
# s=0
ans=0
# for i in arr:
#     if i%2!=0:
#         ans+=1
# for i in range(n):
#     s+=arr[i]
#     # if i>0 and s%2!=0:
#     #     ans+=1
#     pre[i]=s
# # # print(pre)
# # suf=[0]*n
# # s2=0
# # for i in range(n-1,-1,-1):
# #     s2+=arr[i]
# #     suf[i]=s2
# # print(pre,suf)
# # for i in range(n-1,-1,-1):
# #     if (pre[i]-suf[i])%2!=0:
# #         ans+=1
# # print(ans)
even,odd=0,0
# for i in range(len(pre)):
#     if pre[i]%2==0:
#         even+=1
#     else:
#         odd+=1
#     ans+=odd
# print(ans)  

for i in arr:
    ans+=i
    if ans%2:
        odd+=1
        ans+=even+1
    else:
        even+=1
        ans+=odd
print(ans%mod)