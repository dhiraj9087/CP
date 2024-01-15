def main():
    nums = [1,5,3,9,8]
    limit = 2
    # nums = [1,7,6,18,2,1]
    # limit = 3
    # nums = [1,7,28,19,10]
    # limit = 3
    nums=[1,60,34,84,62,56,39,76,49,38]  #[1,56,34,84,60,62,38,76,49,39]
    limit=4
    n = len(nums)
    a=[]
    for i in range(n):
        a.append([nums[i],i])
    a=sorted(a,key=lambda x:x[0])
    print(a)
    c=[[a[0]]]
    for i in range(1,n):
        if a[i][0]-a[i-1][0]<=limit:
            c[-1].append(a[i])
        else:
            c.append([a[i]])
    print(c)
    for i in c:
        arr=[]
        for u,v in i:
            arr.append(v)
        arr.sort()
        for j in range(len(arr)):
            nums[arr[j]]=i[j][0]
    print(nums)
print(main())