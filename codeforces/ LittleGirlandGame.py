s=input()
d={}
for i in s:
    d[i]=s.count(i)
# print(d)
c=0
for i in d.keys():
    if d[i]%2!=0:
        c+=1
# print(c)
if (c-1)%2==0 or c==0:
    print("First")
else:
    print("Second")