# n=int(input())
# d=[]
# for i in range(n):
#     a,b=map(int,input().split())
#     d.append((a,b))
# sorted(d)
# print(d)
# c=0
# q,diff=[],[]
# for i in range(n):
#     diff.append(d[i][1]-d[i][0])
# print(diff)
# # for i in range(n):
# #     for j in range(i+1,n):
# #         if d[i][0]<=d[j][0] and d[i][1]>=d[j][1]:
# #             c+=1
# #             q.append((d[j][0],d[j][1]))
# # print(c)
# # print(set(q))
# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     s1, s2 = set(), set()
#     v = []
#     for i in range(n):
#         a, b = map(int, input().split())
#         s1.add(a)
#         s2.add(b)
#         v.append((a, b))
#     print(v)
#     print(s1)
#     print(s2)
#     mini = min(s1)
#     maxi = max(s2)
#     res = (mini, maxi)
#     print(res)
#     count = 0
#     t = False
#     for it in v:
#         count += 1
#         if it == res:
#             t = True
#             print(count)
#             break
#     if not t:
#         print(-1)

# if __name__ == '__main__':
#     solve()

n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
mi = min(a)
ma = max(b)
f = False
for i in range(n):
    if a[i] == mi and b[i] == ma:
        m = i + 1
        f = True
        break
if f:
    print(m)
else:
    print(-1)