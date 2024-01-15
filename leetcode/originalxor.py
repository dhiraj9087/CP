pref = [5,2,0,3,1]
# [5,7,2,3,2]
n=len(pref)
ans=[0]*n
ans[0]=pref[0]
for i in range(1,n):
    ans[i]=pref[i-1]^pref[i]
print(ans) 