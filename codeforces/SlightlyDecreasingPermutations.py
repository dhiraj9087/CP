# n,k=map(int,input().split())
# a=list(range(1,n+1))
# # a.sort(reverse=True)
# print(*a)
# # for i in range(k,0,-1):
# #     q.append(i)
# # print(q)
# # 1 2 3 4 5 6
# # 1 4 3 6 5 
n, k = map(int, input().split())
q=[]

for i in range(n, n-k, -1):
    q.append(i)
for i in range(1, n-k+1):
    q.append(i)
print(*q)
