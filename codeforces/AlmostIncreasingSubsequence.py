n,q=map(int,input().split())
a=list(map(int,input().split()))
ar=[]
c=0
dp=[0]*n

for i in range(2,n):
    if a[i]<=a[i-1] and a[i-1]<=a[i-2]:
        c+=1
        # print(a[i],a[i-1],a[i-2])
        # print(i-1,i,i+1)
        dp[i-2]=1
        dp[i-1]=1
        dp[i]=1
print(c,dp)
for i in range(q):
    l,r=map(int,input().split())
    # for i in range(l-1,r-1):
    flag=True
    ans=r-l+1
    # while flag:
        # if sum(dp[l-1:r])>2:
        #     # print(sum(dp[l-1:r]))
        #     r=r-1
        #     ans-=1
        # else:
        #     flag=False
    cone=0
    for i in range(l-1,r):
        if dp[i]==1:
            cone+=1
    if cone<3:
        print(r-l+1)
        flag=False
        break
    else:
        r=r-1


            

    # print(l,r,ans)

#     ar.append((l,r))
# print(ar)
