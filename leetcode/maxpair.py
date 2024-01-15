pairs = [[1,2],[7,8],[4,5]]
# pairs = [[1,2],[2,3],[3,4]]
n=len(pairs)

c=0

a = sorted(pairs, key=lambda x: x[1])
print(a)

ans=float('-inf')
for i in range(n):
    if a[i][0]>ans:
        ans=a[i][1]
        c+=1
print(c)



