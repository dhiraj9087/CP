def main():
    # nums = [3,2,3,2,3]
    # nums = [10,10,10,3,1,1]
    # nums=[3,3,3,3,3,1,1]
    nums=[1,1,3,3,1,1,2,2,3,1,3,2]
    nums.sort()
    print(nums)
    n=len(nums)
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    mini=min(d.values())
    maxi=mini+1
    ans=0
    print(d,mini,maxi)
    a=[]
    for i,j in d.items():
        a.append([j,i])
    a.sort(reverse=True)
    print(a)
    grp=0
    for i in range(len(a)):
        if a[i][0]<=maxi:
            ans+=1
        else:
            if a[i][0]%maxi==0:
                ans+=(a[i][0]//maxi)
            else:
                ans+=(a[i][0]//maxi + 1)
    print(ans)

main()