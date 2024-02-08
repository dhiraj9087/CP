def sub(ind,ans,arr,n):
    if ind==n:
        if sum(ans)==tar:
            print(*ans)
            return True
        return False
    ans.append(arr[ind])
    if sub(ind+1,ans,arr,n)==True:
        return True
    ans.pop()
    if sub(ind+1,ans,arr,n)==True:
        return True
    return False



arr=[1,2,1]
tar=2
n=len(arr)
ans=[]
sub(0,ans,arr,n)