n1,n2=map(int,input().split())
k,m=map(int,input().split())
a,b=list(map(int,input().split())),list(map(int,input().split()))
print("YES" if a[k-1]<b[n2-m] else "NO")
# q1,q2=[],[]
# for i in range(k):
#     q1.append(a[i])
# for i in range(m):
#     q2.append(b[i])
# print(q1,q2)
# if q1[k-1]<q2[0]:
#     print("YES")
# else:
#     print("NO")

    