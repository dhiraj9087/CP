chars = ["a","a","b","b","c","c","c"]
c=1
a=[]
n=len(chars)
for i in range(1,n):
    if chars[i]==chars[i-1]:
        c+=1
    else:
        a.append((chars[i-1],c))
        c=1
a.append((chars[-1],c))
print(a)
