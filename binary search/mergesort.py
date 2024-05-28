a=[3 ,4 ,1, 6, 2, 5, 7]
b=[4 ,3 ,1 ,2]
def merge(arr,l,mid,r):
    low=l
    high=mid+1
    temp=[]
    while low<=mid and high<=r:
        if arr[low]<=arr[high]:
            temp.append(arr[low])
            low+=1
        else:
            temp.append(arr[high])
            high+=1
    while low<=mid:
        temp.append(arr[low])
        low+=1
    while high<=r:
        temp.append(arr[high])
        high+=1
    for i in range(l,r+1):
        arr[i]=temp[i-l]


def mergesort(arr,l,r):
    if l==r:
        return
    mid=(l+r)//2
    mergesort(arr,l,mid)
    mergesort(arr,mid+1,r)
    merge(arr,l,mid,r)


mergesort(a,0,len(a)-1)

print(a)