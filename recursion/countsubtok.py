def sub(ind,arr,n,s):
    if ind==n:
        if s==tar:
            return 1
        return 0
    # ans.append(arr[ind])
    s+=arr[ind]
    l=sub(ind+1,arr,n,s)
    s-=arr[ind]
    # ans.pop()
    r=sub(ind+1,arr,n,s)
    return l+r



arr=[1,2,1]
tar=2
s=0
n=len(arr)
# ans=[]
print(sub(0,arr,n,s))