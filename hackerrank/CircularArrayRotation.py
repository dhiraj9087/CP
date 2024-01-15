n,k,q=map(int,input().split())
lst=list(map(int,input().split()))
e=[]
for i in range(q):
    w=int(input())
    e.append(w)
#print(e)
# a=[]
# for i in range(len(lst)-1):
#     a[i]=a[len(lst)-1]
#     a[i+1]=a[i]
#     a[i+2]=a[i+1]
# print()
for i in range(k):
    lst.insert(0,lst[n-1])
    z=len(lst)
    lst.pop(z-1)
#print(lst)
for i in e:
     print(lst[i])