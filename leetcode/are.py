def main():
    nums1 = [3,2,0,1,0]
    nums2 = [6,5,0]
    # nums1 = [2,0,2,0]
    # nums2 = [1,4]
    nums1=[0,17,20,17,5,0,14,19,7,8,16,18,6]
    nums2=[21,1,27,19,2,2,24,21,16,1,13,27,8,5,3,11,13,7,29,7]
    n,m=len(nums1),len(nums2)
    add1,add2=sum(nums1),sum(nums2)
    zero1,zero2=nums1.count(0),nums2.count(0)
    print(add1,add2,zero1,zero2)
    add1+=zero1
    add2+=zero2
    if add1!=add2 and (zero1==0 or zero2==0):
        print(-1)
    if add1==add2:
        print(add1)
    if add1<add2:
        if zero1>0:
            print(add2)
        else:
            print(-1)
    else:
        if zero2>0:
            print(add1)
        else:
            print(-1)
print(main())

