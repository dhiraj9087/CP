s=input()
a,q='hello',''
for i in s:
    if i in a:
        q=q+i
# print(q)
i,j=0,0
while i<len(s) and j<len(a):
        if s[i]==a[j]:
            i+=1
            j+=1
        else:
            i+=1
if j==len(a):
     print("YES")
else:
     print("NO")