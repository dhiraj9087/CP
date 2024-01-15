# # for _ in range((int(input()))):
# #     n=int(input())
# #     d2=[]
# #     for i in range(n):
# #         m,s=map(str,input().split())
# #         d2.append((int(m),s))
# #     # print(d)
# #     d = sorted(d2, key=lambda x: x[0])
# #     # print(d2)
# #     def solve():
# #         c=float('inf')
# #         if d[0][1]=='11':
# #             return d[0][0]
# #         for i in range(1,n):
# #             if (d[i][1]=='10' and d[i-1][1]=='01') or (d[i][1]=='01' and d[i-1][1]=='10'):
# #                 c=min(c,d[i][0]+d[i-1][0])
# #             if d[i][1]=='11':
# #                 c=min(c,d[i][0])
# #         if c==float('inf'):
# #             return -1
# #         else:
# #             return c
# #     print(solve())
# from collections import defaultdict

# def fine():
#     n = int(input())
#     qwe = defaultdict(int)
#     for i in range(n):
#         x, s = input().split()
#         x = int(x)
#         if qwe[s] == 0:
#             qwe[s] = x
#         elif x <qwe[s]:
#             qwe[s] = x
#     # print(qwe)
#     if qwe["11"] == 0:
#         if qwe["01"] == 0 or qwe["10"] == 0:
#             print(-1)
#             # break
#             return
#         else:
#             print(qwe["01"] + qwe["10"])
#             # break
#             return
#     if qwe["10"] == 0 or qwe["01"] == 0:
#         print(qwe["11"])
#         # break
#         return
#     print(min(qwe["01"] + qwe["10"], qwe["11"]))
# for i in range((int(input()))):
#     fine()
t=int(input())
for i in range(t):
    n = int(input())

    d = {}
    while n > 0:
        first,s=map(str,input().split())
        first=int(first)
        if s not in d:
            d[s] = first
        elif first < d[s]:
            d[s] = first
        n -= 1

    if "11" not in d:
        if "01" not in d or "10" not in d:
            print(-1)
        else:
            print(d["01"] + d["10"])
    elif "10" not in d or "01" not in d:
        print(d["11"])
    else:
        print(min(d["01"] + d["10"], d["11"]))