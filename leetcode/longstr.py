from collections import defaultdict
# words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
s=sorted(words,key=lambda x:len(x))
print(s)
n=len(s)
d=defaultdict()
ans=0
for i in s:
    d[i]=1
    for j in range(len(i)):
        a=i[:j]+i[j+1:]
        if a in d:
            d[i] = max(d[i],d[a]+1)
        ans=max(ans,d[i])
print(ans)

