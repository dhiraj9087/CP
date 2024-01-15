s1=input()
s2=input()
c=0
for i in s2:
    if i not in s1:
        c+=1
if c==0:
    print("YES")
else: print("NO")