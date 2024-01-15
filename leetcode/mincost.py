s = "adaa"
chars = "d"
vals = [-1000]
s="kqqqqqkkkq"
chars="kq"
vals=[-6,6]
n=len(s)
ans=[0]*n
ind=0
for i in range(n):
    if s[i] not in chars:
        ans[i]=ord(s[i])-96
    else:
        ind=chars.index(s[i])
        ans[i]=vals[ind]
maxi=ans[0]
curr=ans[0]
for i in range(1,n):
    if ans[i]>curr+ans[i]:
        curr=ans[i]
    else:
        curr+=ans[i]
print(curr)        
# if curr<0:
#     return 0
# return curr