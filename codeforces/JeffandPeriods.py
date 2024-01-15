# n=int(input())
# a=list(map(int,input().split()))
# d={}
# for i in range(len(a)):
#     d[a[i]]=a.count(a[i])
# # print(d)
# z=[]
# for i in range(len(a)):
#     q=a[i]
#     for j in range(i+1,len(a)-i):
#         if a[j]==q:
#             z.append([a[i],j-i])
#             # break
# print(z)
# d1=list(d.keys())
# d1.sort()
# d2={i:d[i] for i in d1}
# print(d2)
# for i in d2.keys():
#     if i in z[0]:
#         print(i,z[i][0])
#     else:
#         print(i,0)
# print(len(d))
# # for i in d.keys():
# for i in d2.keys():
#     if d2[i]!=1:
#         print(i,n//d2[i])
#     else:
#         print(i,0)

from collections import defaultdict
n = int(input())
mp = defaultdict(list)
a=list(map(int,input().split()))
for i in a:
    mp[i].append(i)
print(mp)
v = []
for k in mp.keys():
    print(len(mp[k]))
    if len(mp[k]) == 1:
        v.append((k, 0))
    else:
        s = set()
        for i in range(1, len(mp[k])):
            s.add(abs(mp[k][i] - mp[k][i-1]))
        if len(s) == 1:
            v.append((k, s.pop()))

# print(len(v))
# for i in range(len(v)):
#     print(v[i][0], v[i][1])