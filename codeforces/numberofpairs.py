# for i in range((int(input()))):
#     n,k=map(int,input().split())
#     a=input()
#     s=""
#     for i in a:
#         if ord(i)>=97:
#             s=s+i
#     for i in a:
#         if i not in s:
#             s=s+i
#     # print(s)
#     # s=""
#     d={}
#     c=0
#     for i in s:
#         if ord(i)>=97:
#             d[i]=a.count(i),a.count(chr(ord(i)-32))
#         else:
#             if chr(ord(i)+32) not in d:
#                 d[i]=a.count(chr(ord(i)+32)),a.count(i)
#     # print(d)
#     for i in d:
#         v1,v2=d[i]
#         if v1!=1 and v1==v2:
#             c=v1
#             d[i]=0,0
#         elif v1>=1 and v2>=1:
#             c+=1
#             d[i]=v1-1,v2-1
#     for i in d:
#         v1,v2=d[i]
#         if v1 - v2 >1 or v2>1:
#             if (v1+v2)//2<=k:
#                 c=c+((v1+v2)//2)
#                 k-=1
#         # elif v2>1:
#         #     c=c+((v1+v2)//2)
#         #     k-=1
#     print(c)
import string
def solve():
    N = 26
    n, k = map(int, input().split())
    s = input()
    big = [0] * N
    small = [0] * N
    for i in s:
        if i in string.ascii_uppercase:
            big[ord(i) - ord('A')] += 1
        else:
            small[ord(i) - ord('a')] += 1
    # print(big,small)
    answer = 0
    for i in range(N):
        pairs = min(small[i], big[i])
        answer += pairs
        small[i] -= pairs
        big[i] -= pairs
        add = min(k, max(small[i], big[i]) // 2)
        k -= add
        answer += add
    print(answer)
t = int(input())
for _ in range(t):
    solve()
