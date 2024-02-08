def sub(ind,ans,arr,n,s):
    if ind==n:
        if s==tar:
            print(*ans)
        return
    ans.append(arr[ind])
    s+=arr[ind]
    sub(ind+1,ans,arr,n,s)
    s-=arr[ind]
    ans.pop()
    sub(ind+1,ans,arr,n,s)



arr=[1,2,1]
tar=2
n=len(arr)
ans=[]
s=0
sub(0,ans,arr,n,s)