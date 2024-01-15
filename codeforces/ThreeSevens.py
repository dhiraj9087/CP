# for _ in range((int(input()))):
#     m=int(input())
#     d,l=[],[0]
#     for i in range(m):
#         n=int(input())
#         a=list(map(int,input().split()))
#         for j in range(len(a)):
#             d.append(a[j])
#         # d.append(a)
#         l.append(n)

#     for i in range(len(l)-1):
#         l[i+1]=l[i]+l[i+1]
#     # print(d)
#     # print(l)
#     ans=[]
#     for i in range(m-1):
#         for j in range(l[i],l[i+1]):
#             # print(d[j])
#             if d[j] not in d[l[i+1]::]:
#                 ans.append(d[j])
#                 break
#     # print(ans)  
#     last=[]
#     for i in range(l[len(l)-2],l[len(l)-1]):
#         # last.append(d[i])
#         if d[i] not in d[l[len(l)-3]:l[len(l)-2]:]:
#             ans.append(d[i])
#     # print(ans)
#     if len(ans):
#         print(*ans)
#     else:
#         print("-1")
#     # for i in range(len(last)):
#     #     if last[i] not in 
#     # for i in range()
#     # q=[]
#     # while m:
#     #     j=0
#     #     for i in range(len(d[j])):
#     #         print(d[j][i])
#     #         # if d[j][i] not in d[j+1::]:
#     #         #     q.append(d[j][i])
#     #     j+=1

 
for i in range((int(input()))):
    m = int(input())
    l = {}
 
    for i in range(m):
        _ = int(input())
        a = list(map(int, input().split()))
 
        for ai in a:
            l[ai] = i 
                      
   
    r = {}
    for id, pos in l.items():
        r[pos] = id
   
    ans = sorted(r.items())
    
    if len(ans) == m:
        print(' '.join(map(str, [v for k, v in ans])))
    else:
        print(-1)
 
