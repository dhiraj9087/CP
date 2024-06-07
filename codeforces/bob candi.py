# import math
# import sys
# input=sys.stdin.readline
# def main():
#     # input1=int(input())
#     # input2=list(map(int,input().split()))
#     # input3=int(input())
#     ans=0
#     can=[]
#     for i in range(input1):
#         if input2[i]%5==0:
#             ans+=1
#         else:
#             can.append(input2[i])
#     can.sort()
#     # print(can)
#     for i in range(len(can)):
#         if can[i]<=input3:
#             ans+=1
#             input3-=can[i]
#     return ans
# SELECT OrderId, Categoryid from cart, category
# where (cart.Bookid=book.Bookid and book.CategoryId=category.Categoryid) and book.Book_Desc in ('Science Fiction','Love')
#     # input1=input().strip()
#     # input2=input().strip()
#     # if input1==input2:
#     #     return input1 + "_Verified"
#     # return input1 + "_NotVerified"
# # for _ in range(int(input())):
# print(main())