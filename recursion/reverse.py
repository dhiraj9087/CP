def rev(l,r):
    if l>r:
        return arr
    arr[l],arr[r]=arr[r],arr[l]
    return rev(l+1,r-1)

arr=[3,2,5,8,1]
print(rev(0,len(arr)-1))
# print(arr)