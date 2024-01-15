# import math
# import sys
# input=sys.stdin.readline
# def main():
#     n = int(input())
#     v = [0] + list(map(int, input().split()))
#     mp = {}
#     ind = {}

#     for i in range(1, n + 1):
#         if v[i] not in mp:
#             if i == 1:
#                 mp[v[i]] = 1
#             else:
#                 mp[v[i]] = i - 1
#         else:
#             cmp = (i - mp[v[i]]) // 2
#             mp[v[i]] = max(mp[v[i]], cmp)
#         ind[v[i]] = i

#     a, b = 0, 0
#     mini = float('inf')

#     if len(mp) == 1:
#         print(v[1], 0)
#         return

#     for i in ind:
#         cmp = n - ind[i]
#         mp[i] = max(cmp, mp[i])

#     for i in mp:
#         if mp[i] < mini:
#             mini = mp[i]
#             a, b = i, mp[i]

#     print(a, b)
#     # n=int(input())
#     # a=list(map(int,input().split()))
#     # d={}
#     # for i in a:
#     #     if i in d:
#     #         d[i]+=1
#     #     else:
#     #         d[i]=1
#     # d2= dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
#     # d3 = {}
#     # for key, value in d2.items():
#     #     d3.setdefault(value, []).append(key)
#     # # print(d3,d2)
#     # # a=[]
#     # it=iter(d3.items())
#     # item=next(it)[1]
#     # print(item)
    
#     # for i in range(len(item)):
#     #     left,right=-1,n+1
#     #     l,r=0,n-1
#     #     while l<n:
#     #         if a[l]==item[i]:
#     #             left=i
#     #             break
#     #         else:
#     #             l+=1
#     #     while r>0:
#     #         if a[r]==item[i]:
#     #             right=i
#     #             break
#     #         else:
#     #             r-=1
        


# for _ in range(int(input())):
#    main()