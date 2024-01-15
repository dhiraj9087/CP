n = 5
k = 4
# n = 2
# k = 6
# a=[i for i in range(1,n+1)]
# print(a)
i=1
a=set()
ans=[]
while len(ans)<n:
    if (i not in a) :
        if k-i not in a:
            a.add(i)
            ans.append(i)
    i+=1
