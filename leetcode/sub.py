s = "165462"
k = 60
# s = "238182"
# k = 5
r=0
n=len(s)
a=""
a+=s[0]
flag=False
ans=0
while r<n:
    maxi=0
    l=r
    while l<n and maxi<=k:
        maxi=max(maxi,int(s[r:l]))
        if maxi<=k:
            l+=1
    if maxi>k:
        print(-1)
        break
    r=l
    ans+=1
print(ans)


