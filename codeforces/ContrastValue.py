# def solve():
#     n=int(input())
#     a=list(map(int,input().split()))
#     s=0
#     b=list(a)
#     for i in range(1,n):
#         s+=abs(a[i]-a[i-1])
#         # diff.append(abs(a[i]-a[i-1]))
#     # diff.sort()
#     # print(s,diff)
#     a.sort()
#     # b.sort(reverse=True)
#     # print(a,b)
#     c=[]
#     for i in range(n//2):
#         c.append(a[n-i-1])
#         c.append(a[i])
#     if n%2==1:
#         c.append(a[n//2])
#     # print(c,s)
#     if len(set(c))==1:
#         print(1)
#         return
#     contrast=0
#     for i in range(1,n):
#         contrast+=abs(c[i]-c[i-1])
#         if contrast==s:
#             print(i+1)
#             return
# for _ in range((int(input()))):
#     solve()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flag = []
    count = 1
    for i in range(n-1):
        if (a[i] != a[i+1]):
            if (a[i] - a[i+1] < 0):
                flag.append('-')
            else:
                flag.append('+') 
    if len(flag) == 0:
        print(1)
    else:
        for i in range(len(flag) - 1):
            if flag[i] != flag[i+1]:
                count += 1
        print(count + 1)
 
