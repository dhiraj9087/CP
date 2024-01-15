# for i in range((int(input()))):
#     n,a,b=map(int,input().split())
#     q=[i for i in range(1,n+1)]
#     # print(q)
#     d=[b]
#     for i in range(1,n//2+1):
#         if i != a and i not in d:
#             d.append(i)
#             q.remove(i)
#     # print(d)
#     # l=[]

#     # d.append(a)
#     # for i in range(n//2):
#     #     if a+i !=b and a+i not in d:
#     #         l.append(a+i)
#     l=[]
#     i=0
#     c=n//2
#     # print(c)
#     while c>0:
#         if a+i != b and a+i not in d:
#             l.append(a+i)
#             q.remove(a+i)
#         i+=1
#         c-=1
#     # print(q)
#     for i in q:
#         if i not in d and i not in l:
#             l.append(i)
#     # print(l)
#     ans=list(l+d)
#     # print(*ans)
#     if a!=min(l) or b!=max(d):
#         print("-1")
#     else:
#         print(*ans)
# t = int(input())
for i in range((int(input()))):
    n, a, b = map(int, input().split())
    d = [a]
    for j in range(n, 0, -1):
        if j != a and j != b:
            d.append(j)
    # print(p)
    d.append(b)
    if(len(d) == n and min(d[0:n//2]) == a and max(d[n//2:n]) == b):
        print(*d)
    else:
        print(-1)
    