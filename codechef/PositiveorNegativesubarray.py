# for _ in range((int(input()))):
#     n=int(input())
#     b=list(map(int,input().split()))
#     a=[2**(i-1) for i in range(1,n+1)]
#     # print(a)
#     c=[a[i]*b[i] for i in range(n)]
#     # print(c)
#     pos,neg=0,0
#     sum=0
#     for i in range(len(c)):
#         if c[i]>0:pos+=1
#         else:neg+=1
#     for i in range(n):
#         for j in range(i+1,n):
#             sum+=c[j]
#             if sum>0: pos+=1
#             elif sum<0: neg+=1
#     # print(pos,neg)
#     print(abs(pos-neg))
# cook your dish here

# for i in range((int(input()))):
#     n=int(input())
#     b=list(map(int,input().split()))
#     subarray=(n*(n+1))//2
#     poscount=0
#     for i in b:
#         if i>0:
#             poscount+=1
#     a=[]
#     for i in range(n):
#         if(b[i]==-1):
#             a.append(i+1)
#     s=sum(a)
#     # print(a)
#     if(poscount==n):
#         print(subarray)
#     else:
#         pos=subarray-s
#         print(abs(s-pos))
# cook your dish here

t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    p, q = 0, 0
    for i in range(n-1, -1, -1):
        if b[i] == 1:
            p += i+1
        else:
            q += i+1
    # print(p,q)
    print(abs(p-q))
