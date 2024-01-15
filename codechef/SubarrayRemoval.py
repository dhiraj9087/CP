# for _ in range((int(input()))):
#     n=int(input())
#     a=list(map(int,input().split()))
#     # c,count=0,0
#     # for i in range(n-1):
#     #     if a[i]<a[i+1]:
#     #         c+=1
#     #     count=max(count,c)
#     # print(count)
#     dict={}
#     for i in range(len(a)):
#         dict[a[i]]=i+1
#     # print(dict)
#     per=0
#     for i in dict:
#         if i>=dict[i]:
#             per+=1
#     print(per-1)
for _ in range((int(input()))):
    n = int(input())
    arr = list(map(int,input().split()))
    if sorted(arr)==arr:
        print(n-1)
    else:
        # l = 0 
        # r = n - 1
        # size = 0
        # maxi = 0
        # while l<r:
        #     a,b = arr[l],arr[r]
        #     if a<b:
        #         maxi = max(maxi,a)
        #         l += 1
        #     else:
        #         maxi = max(maxi,b)
        #         r -= 1
        #     size += 1
        #     if size==maxi:
        #         break
        # print(n-size)
        for i in range(1,n):
            for j in range(i+1,n):
                if arr[j]>arr[i]:
    
