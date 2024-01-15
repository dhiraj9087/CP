# n,k=map(int,input().split())
# a=list(map(int,input().split()))
# # flag,c=0,0
# # z=len(a)
# # while(z):
# #     # if len(set(a[k-1::]))==1:
# #     #     if len(set(a))==1:
# #     #         print("0")
# #     #         flag=3
# #     #         break
# #     # else:
# #     #     flag=0
# #     if len(set(a))==1:
# #         flag=1
# #         break
# #     z-=1
# #     a.append(a[k-1])
# #     a.pop(0)
# #     # print(a)  
# #     c+=1
# #     # if len(set(a))==1:
# #     #     flag=1
# #     #     break
# # if flag==1:
# #     print(c)
# # elif flag==0:
# #     print("-1")
# if len(set(a[k-1::]))==1:
#     print(n-len(a[k-1::]))
# else:
#     print("-1")\
n,k= map(int,input().split())
# k = int(input())
v = list(map(int, input().split()))
cnt = 0
for i in range(n-1, 0, -1):
    if v[i] != v[i-1]:
        break
    cnt += 1
cnt += 1
if k > (n-cnt):
    print(n-cnt)
else:
    print("-1")

