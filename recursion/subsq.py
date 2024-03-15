def sub(ind,ans,arr,n):
    if ind==n:
        print(*ans)
        return
    ans.append(arr[ind])
    sub(ind+1,ans,arr,n)
    ans.pop()
    sub(ind+1,ans,arr,n)



arr=[9,6,4397,492]
n=len(arr)
ans=[]
sub(0,ans,arr,n)
