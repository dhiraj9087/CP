# for i in range((int(input()))):
#     n,m=map(int,input().split())
#     a=list(map(int,input().split()))
#     count1,count2,count=0,0,0
#     q=[]
#     for i in range(n):
#         if a[i]==-1: count1+=1
#         elif a[i]==-2: count2+=1
#         else:  
#             q.append(a[i])
#     count=len(set(q))
#     # print(count1,count2,count,q)
#     w=[0]*m
#     w[q[0]-1]=q[0]
#     index=q[0]-1
#     for i in range(n):
#         if a[i]==-1:
#             w[(q[0]-1)-(i+1)]=-1
#         elif a[i]==-2 and w[index+1]==0:
#             w[index+1]=-2
#             index+=1
#         else:
#             if w[a[i]-1]==0:
#                 w[a[i]-1]==a[i]
#     print(w)

# def solve():
#     n, m = map(int,input().split())
#     a = list(map(int,input().split()))
#     c1 = c2 = 0
#     d = {0, m+1}
#     print(d)
#     for i in a:
#         if i == -1:
#             c1+=1
#         elif i == -2:
#             c2+=1
#         else:
#             d.add(i)
#     # print(d)
#     d = sorted(d)
#     print(d)
#     ans = 0
#     for i in range(len(d)):
#         ans = max(ans, len(d) - 2 + min(d[i] - i, c1) + min(m - d[i] - (len(d) - i - 2), c2))
#     print(ans)
 
# def main():
#     t = int(input())
#     for _ in range(t):
#         solve()
 

# main()

