capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2
# capacity = [10,2,2]
# rocks = [2,2,0]
# additionalRocks = 100
if sum(capacity)<=additionalRocks:
    print(len(capacity))
ans=0
ind=0
arr=[capacity[i]-rocks[i] for i in range(len(rocks))]
arr.sort()
# print(arr)
for i in range(len(capacity)):
    if additionalRocks<=0:
        break
    if arr[i]<=additionalRocks:
        ans+=1
        additionalRocks-=arr[i]
    else:
        break
print(ans)
    # capacity[i]=(capacity[i]-rocks[i])
    # additionalRocks-=capacity[i]
    # ans+=1
    # if additionalRocks<=0:
    #     ind=i
    #     break
# for i in range(ind,len(capacity)):
#     if capacity[i]==rocks[i]:
#         ans+=1
# print(capacity,ans,ind)