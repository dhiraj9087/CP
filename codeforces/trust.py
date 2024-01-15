
# # def trust():
# #     c=0
# #     c0=0
# #     for i in range(n):
# #         if a[i]==n:
# #             c+=1
# #         if a[i]==0:
# #             c0+=1
# #     if c==n:
# #         return -1
# #     elif c0==n:
# #         return 0
# #     else:
# #         return c
# def count_liars():
#     min_liars = sum(l) - n
#     max_liars = sum([n - x for x in l])
#     if max_liars < 0 or min_liars > n:
#         return "Contradiction"
#     return max(0, min(n - sum(l) + max(l), n - max_liars))

    

# for i in range((int(input()))):
#     n=int(input())
#     l=list(map(int,input().split()))
#     print(count_liars())



# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     for i in range(n):
#         liar = 0
#         for j in range(n):
#             if a[i] < a[j]:
#                 liar += 1
#         print(liar)  
#         nliar = 0
#         for j in range(n):
#             if liar < a[j]:
#                 nliar += 1
#         if liar == nliar:
#             print(liar)
#             return
#     print(-1)

# t = int(input())
# for _ in range(t):
#     solve()
def solve():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    # print(v)
    for i in range(n+1):
        c = 0
        for j in range(n):
            if v[j] > i:
                # print(v[j],end=' ')
                c += 1
        if c == i:
            print(c)
            return
    print(-1)

for i in range((int(input()))):
    solve()
