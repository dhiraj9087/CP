# n,k=map(int,input().split())
# a=list(map(int,input().split()))
# m=sum(a[:k:])
# # print(m)
# d=[]
# for i in range(n-k):
#     for j in range(i,i+1):
#         m=min(m,a[j]+a[j+1]+a[j+2])
#         d.append((a[j],m))

# # print(m)
# # for i in d:
# #     if d[i]==m:
# #         print(a.index(i)+1)
# #         break
# # print(d)
# mini=float('inf')
# for i in range(len(d)):
#     if d[i][1]<mini:
#         mini=min(mini,d[i][1])
#         w=d[i][0]
# print(mini)
# # print(a.index(w)+1)

n, k = map(int,input().split())
a = list(map(int,input().split()))
sum = [0] * (n + 1)
minn = 1e9 + 7
ans = 0
for i in range(1, n + 1):
    sum[i] = sum[i - 1] + a[i - 1]
# print(sum)
for i in range(1, n - k + 2):
    if sum[i + k - 1] - sum[i - 1] < minn:
        minn = sum[i + k - 1] - sum[i - 1]
        ans = i
print(ans)


