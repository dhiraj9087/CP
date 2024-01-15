n=int(input())
l=list(map(int,input().split()))
a,b=l[0],l[0]
ai,bi=0,0
for i in range(len(l)):
    if b>=l[i]:
        b=l[i]
        bi=i
    if a<l[i]:
        a=l[i]
        ai=i
if l[0]==max(l) and l[len(l)-1]==min(l):
    print("0")
elif ai>bi:
    print(ai+(len(l)-1-bi)-1)
else:
    print(ai+(len(l)-1-bi))
