# k=int(input())
# s=input()
# a,q,c='',[],0
# for i in s:
#     q.append(s.count(i))
# # if k==1:
# #     print(s)
# # q=set(q)
# q=list(q)
# #print(q)
# if len(q)%k==0:

#     for i in range(len(s)):
#         if s[i] not in a:
#             a=a+s[i]
# # else:
# #     for i in range(len(s)):
# #         if s[i] not in a:
# #             a=s[i]*s[i].count(s[i])
# #     print(a*k,'q1')
# #     # print(a*k)
# for i in range(len(q)):
#     if q[i]%k==0:
#        c+=1
# #print(c)
# if c==len(s):
#     print(a*k)

# else:
#     print("-1")
#     # else:
#     #     print("-1")
#     #     break


    


# # import sys

# # k = int(input())
# # s = input().strip()

# # l = len(s)
# # s = sorted(s)

# # count = 0
# # for i in range(l):
# #     if i % k == 0:
# #         ch = s[i]
# #     if s[i] == ch:
# #         count += 1

# # if l == count and count % k == 0:
# #     for i in range(k):
# #         for l in range(0, len(s), k):
# #             sys.stdout.write(s[l])
# # else:
# #     print("-1")


# k = int(input())
# s = input()
# d = {}
# flag=True
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# # print(d)
# for i in d:
#     if d[i] % k!=0:
#         # print(d[i])
#         print(-1)
#         flag=False
#         break
# if flag:
#     a = ""
#     for i in d:
#         c = d[i] // k
#         a += i * c
#     res = a * k
#     print(res)
gain=[6,9,2,3,4]
loss=[2,4,3,4,5]
query=[8,12,9]
n=5
q=3
d=[]
for i in range(len(gain)):
    d.append(gain[i]-loss[i])
# return d
for i in range(len(d)):
    for j in range(0,len(d)-i-1):
        if d[j]<d[j+1]:
            d[j],d[j+1]=d[j+1],d[j]
# d.sort()
# print(d)
flag=True
ans=[]
# e=sum(d)
ind=[]
# for i in range(q):
#     w=0
#     for j in range(n):
#         w=w+gain[i]-loss[i]
#         if w
#     if e<query[i]:
#         print(query[i])
#         ind.append(i)
# print(ind)
for i in range(q):
    add=0
    for j in range(n):
        add=add+d[j]
        if add>=query[i]:
            ans.append(j+1)
            ind.append(query[i])
            flag=False
            break
    # if j>n:
    #     ans.append(-1)
# print(ind)
one_=[]
for i in range(len(query)):
    if query[i] not in ind:
        # query[i]
        one_.append(i)
# print(one_)
for i in range(len(one_)):
    ans.insert(one_[i],-1)
print(ans)