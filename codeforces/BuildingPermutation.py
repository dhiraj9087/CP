n=int(input())
a=list(map(int,input().split()))
a.sort()
# print(a)
c=0
for i in range(n):
    c=c+(abs(a[i]-(i+1)))
print(c)