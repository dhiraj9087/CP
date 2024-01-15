# n,m=map(int,input().split())
# q,a=[],[]
# for i in range(m):
#     s=input()
#     q.append(s)
# # print(q)
# # print(len(q[0]))
# for i in range(len(q)):
#     for j in range(len(q[i])):
#         if q[i][j]=='.':
#             if (i+j)%2==0:
#                 a.append('B')   
#             else:
#                 a.append('W')
#         else:
#             a.append('-')
# # print(a)
# # for i in range(len(a)//2-1):
# #     if a[i]=='B' and a[i+n]=='B':
# #         a[i]='W'
# #     elif a[i]=='W' and a[i+n]=='W':
# #         a[i]='B'
# # print(a)
# for i in range(n):
#     for j in range(m):
#         idx = i * m + j
#         if idx < len(a):
#             print(a[idx], end='')
#         else:
#             print(' ', end=' ')
#     print()
import sys
import queue
input = sys.stdin.readline
n, m = map(int, input().split())
mp = []
for i in range(n):
    mp.append(list(input().strip()))
# print(mp)
for i in range(n):
    for j in range(m):
        if mp[i][j] == '.':
            if (i+j)%2 == 0:
                mp[i][j] = 'B'
            else:
                mp[i][j] = 'W'
for i in range(n):
    print(''.join(mp[i]))

