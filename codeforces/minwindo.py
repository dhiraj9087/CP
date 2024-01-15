from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"
l,r=0,0
n=len(s)
ans=[]
a,b=Counter(),Counter(t)
while r<n:
    a[s[r]]+=1
    r+=1
    if a&b!=b:
        continue
    while l<r:
        a[s[l]]-=1
        l+=1
        if a&b==b:
            continue
        ans.append(s[l-1:r])
        break
print(a,b,min(ans,key=len))
