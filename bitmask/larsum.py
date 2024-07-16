a=[-2, -3, 4, -1, -2, 1, 5, -3]
ans=0
maxi=0
l,m=0,0
for i in range(len(a)):
    if maxi==0:
        l=i
    maxi+=a[i]
    if ans<maxi:
        ans=maxi
        m=i
    if maxi<0:
        maxi=0
print(ans,a[l:m+1])