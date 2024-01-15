# for i in range((int(input()))):
#     n,x=map(int,input().split())
#     a=list(map(int,input().split()))
#     # q=[]
#     flag=True
#     # while flag:
#     #     if x not in a:
#     #         print(x)
#     #         flag=False
#     #     else:
#     #         x=x-1
#     #         q=[]
#     #         for i in range(n):
#     #             q.append(x|a[i])
#     #         if len(set(q))<2:
#     #             x=x-1
#     # x=x+1
#     # # y=1
#     # while flag:
#     #     x=x-1
#     #     q=set()
#     #     for i in range(n):
#     #         q.add(x|a[i])
#     #         if len(q)>1:
#     #             flag=False
#         # print(q)
#     for i in range(31):
#         q=set()
#         for j in a:
#             z=j>>i & 1
#             q.add(z)
#             if len(q)==2:
#                 break
        

        
#     print(q)
#         # y+=1
        
# for i in range(int(input())):
#     n, x = map(int, input().split())
#     a = list(map(int, input().split()))

#     mask = 0
#     for j in range(n):
#         mask |= a[j]

#     ans = x
#     for j in range(n):
#         y = a[j] | x
#         ans = min(ans, y ^ mask)

#     print(ans)


    




