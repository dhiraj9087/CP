def fun(ind,s,path,ans):
    if ind==len(s):
        ans.append(path[:])
        return
    for i in range(ind,len(s)):
        if s[ind:i+1]==s[ind:i+1][::-1]:
            path.append(s[ind:i+1])
            fun(i+1,s,path,ans)
            path.pop()
s = "aab"
ans=[]
path=[]
fun(0,s,path,ans)
print(ans)
