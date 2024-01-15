s,n=map(int,input().split())
d,c=[],0
for i in range(n):
    x,y=map(int,input().split())
    d.append((x,y))
#print(d)
d.sort()
# print(d)
for i in d:
    # print(i[1])
    if i[0]<s:
        s=s+i[1]
        c+=1
# sorted_dict = dict(sorted(d.keys()))
if c==n:
    print("YES")
else:
    print("NO")
# print(c)