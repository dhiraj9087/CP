arr = [1024,512,256,128,64,32,16,8,4,2,1]
d=[]
for i in arr:
    a=bin(i)
    d.append((a.count('1'),i))

# print(d1)
d.sort()
ans=[]
for i,j in d:
    ans.append(j)
print(ans)
