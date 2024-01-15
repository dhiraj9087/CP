# import math
# for i in range((int(input()))):
#     a,b=map(int,input().split())
#     q=[]
#     c=0
#     # for i in range(a,b+1):
#     #     q.append(i)
#     #print(q)
#     #for i in range(len(q)):
#     # while(math.sqrt(q[i])):
#     #         c+=1
#     #         i+=1
#     # print(c)
#     #print(math.sqrt(4))
#     for i in range(a,b+1):
#         w=int(math.sqrt(i))
#         if(w*w==i):
#             c+=1
#             #print(i)
#     print(c)
def re(n,k):
    
    return (n>>k)

n=int(input())
k=int(input())
re(n,k)