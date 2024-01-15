gain = [-5,1,5,0,-7]
n=len(gain)
ans=[0]*(n+1)
s,maxi=0,float('-inf')
for i in range(n):
    s+=gain[i]
    maxi=max(s,maxi)
print(maxi)
        