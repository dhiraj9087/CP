# n=int(input())
# a=list(map(int,input().split()))
# # d={}
# a.sort(reverse=True)
# print(a)
# # q1,q2,q3=[],[],[]
# # s,c=0,a.count(4)
# # for i in range(n):
# #     if a[i]==1:
# #         q1.append(a[i])
# #     if a[i]==2:
# #         q2.append(a[i])
# #     if a[i]==3:
# #         q3.append(a[i])
# # print(q1,q2,q3)
# # m=min(len(q1),len(q3))
# # # for i in range(m):
# # #     q1.append(q3[i])
# # del q3[:m]
# # w,m1=0,0
# # if len(q2)%2==0:
# #     m1=len(q2)//2 
# # else:
# #     m1=len(q2)//2 + 1
# # # print(q1,q2,q3,m1)
# # print(c+len(q1)+len(q3)+m1)
# # for i in range(n):
# #     s+=a[i]
# #     if s==4:
# # count_3=a.count(3)
# # count_2=a.count(2)
# # count_1=a.count(1)
# # print(count_3,count_2,count_1)
# s,c=0,0
# for i in range(len(a)):
#     s+=a[i]
#     if s==4:
#         c+=1
#         s=0
#     elif s>4:
#         c+=1
#         # print(s)
#         s=s-4
#     # elif s<4:
# print(c)

n = int(input())
arr =list(map(int,input().split()))
arr.sort()
# print(arr)
taxi, k, i = 1, 0, n-1
while k != i:
    if arr[i] + arr[k] <= 4:
        arr[i] += arr[k]
        k += 1
    
    else:
        i -= 1
        taxi += 1
# print(arr)
print(taxi)

