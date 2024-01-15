# # # cook your dish here
for i in range((int(input()))):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
# #     # for i in range(n):
# #     #     if a[i]==1 and b[i]==0:
# #     #         print("NO")
# #     #         break
# #     #     elif 1 not in a:
# #     #         print("NO")
# #     #         break
# #     #     elif a[n-1]==0 and b[n-1]==1:
# #     #         print("NO")
# #     #     else:
# #     #         print("YES")
# #     #         break
# #     a1=a.count(1)
# #     b1=b.count(1)
# #     # print(a1,b1)
# #     if a1%2==0 and b1%2==0:
# #         print("YES")
# #     else:
# #         print("NO")
   
   
    
#     # for i in range(n-2):
#     #     if A[i+1]!=B[i+1]:
#     #         A[i+1]=A[i] | A[i+1] | A[i+2]
#     
#     # elif A==B:
#     #     print("YES")
#     # else:
#     #     print("NO")
    w=0
    if A[0] != B[0] or A[n-1] != B[n-1]:
        print("NO")
        continue

    ones_count = A.count(1)

    for i in range(1, n-1):
        if A[i] != B[i] and A[i] == 0 and ones_count == 0:
            print("NO")
            w = 1
            break
        elif A[i] != B[i] and A[i] == 1:
            print("NO")
            w = 1
            break

    if w == 0:
        print("YES")

    # else:
    #     print("NO")

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     if a[0] != b[0]:
#         print("no")
#         return
#     if a[n - 1] != b[n - 1]:
#         print("no")
#         return
#     acnt = 0
#     bcnt = 0
#     for i in range(n):
#         if a[i] == 0:
#             acnt += 1
#         else:
#             bcnt += 1
#     for i in range(1, n - 1):
#         if a[i] != b[i] and a[i] == 0 and bcnt == 0:
#             print("no")
#             return
#         if a[i] != b[i] and a[i] == 1:
#             print("no")
#             return
#     print("yes")
#     return


    


