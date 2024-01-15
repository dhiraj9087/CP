# import math
# import sys
# input=sys.stdin.readline
# def main():
#     n,k=map(int,input().split())
#     s=set()
#     l=[]
#     for i in range(1,n+1):
#         s.add(i)
#         l.append(i)
#     ind=k%n - 1
#     ans=[]
#     while s:
#         val=l[ind]
#         s.remove(val)
#         l.remove(val)
#         ans.append(val)
#         if s:
#             ind=(ind+k)%n -1 
#     print(*ans)

# # for _ in range(int(input())):
# main()
#1100
#0101
# 11 
#0110 - 6
#0111 - 7
#11001
#0001
#0110
#1110
n=4
for i in range(n-1,-1,-1):
    v=1<<i
    print(bin(v),12|v,5|v)
# print(1<<6)

