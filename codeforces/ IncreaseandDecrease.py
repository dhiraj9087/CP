# n=int(input())
# a=list(map(int,input().split()))
# c=0
# q,d=[],{}
# for i in range(n-1):
#     q.append(abs(abs(a[i])-abs(a[i+1])))
# # print(q)
# for i in q:
#     d[i]=q.count(i)
# print(d)
# import sys
# a = int(sys.stdin.readline())
# t = sum(map(int, sys.stdin.readline().split()))
# print(t)
# print(a-1 if t % a else a)
n=int(input())
a=sum(list(map(int,input().split()))) 
print(n-1 if a%n else n)
