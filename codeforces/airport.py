# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# # a.sort()
# w=list(a)
# c=0
# i=0
# for i in range(n-m):
#     c+=(a[i]-1)
# # print(c)
# max_sum=sum(a)+c
# # print(max_sum)
# min_sum=0
# for i in range(len(a)):
#     while(a[i]>0 and n>=0):
#         n=n-w[i]
#         # print(n)
#         min_sum+=(a[i])
#         a[i]=a[i]-1
# print(max_sum,min_sum+1)