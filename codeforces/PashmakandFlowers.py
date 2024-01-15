n=int(input())
a=list(map(int,input().split()))
a.sort()
q=a[n-1]-a[0]
# print(a,q)
c=0
if a[0]==a[n-1]:
    print(q,(n-1)*n//2)
else:
    x,y=1,1
    for i in range(1,n-1):
        if a[i]==a[0]:
            x+=1
        elif a[i]==a[n-1]:
            y+=1
    print(q,x*y)
# for i in range(n):
#     for j in range(i+1,n):
#         if abs(a[i] - a[j])>=q:
#             c+=1
# print(q,c)
# for i in range(n):
#     if abs(a[i]-a[n-1-i])==q:
#         c+=1
# print(c)
# if n<=3:
#     print(q,c)
# else:
#     print(q,c+2)


