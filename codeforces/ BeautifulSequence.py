# s=input()
# a=[]
# n=len(s)
# d = {str(i-96):chr(i) for i in range(97, 123)}
# # print(d)
# for i in range(n-1):
#     num=int(s[i:i+2])
#     if num<=26:
#         a.append([num,i,i+1])
# print(a,ord('a'))
# ans1=''
# for i in s:
#     ans1+=d[i]
# print(ans1)
# ans=[]
# for i in range(len(a)):
#     x,y,z=a[i]
    
#     ele=""
#     for j in range(0,y+1):
#         if j>0:
#             ele+=d[str(j)]
#     ele+=d[str(x)]
#     for j in range(z+1,n):
#         if j>0:
#             ele+=d[str(j)]

#     ans.append(ele)
# print(ans)
res=1
a=1
for i in range(2):
    res=res*4
    a=(a*4)%10
    print(res,a)
print(5**5)