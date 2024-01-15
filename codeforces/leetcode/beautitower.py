# maxHeights = [5,3,4,1,1]    #[5,3,3,1,1].
# h = [6,5,3,9,2,7]    #[3,3,3,9,2,2].
# maxHeights = [3,2,5,5,2,3]     #[2,2,5,5,2,2].
maxHeights=[1,1,4,3,3,3,6]
# n=len(maxHeights)
# maxi=max(maxHeights)
# ind=maxHeights.index(maxi)
# add=sum(maxHeights)
ans=0
# print(ind)
# for i in range(ind,0,-1):
#     print(maxHeights[i])
#     if maxHeights[i]<maxHeights[i-1]:
#         maxHeights[i-1] -= (maxHeights[i-1]-maxHeights[i])
#         # add -= (maxHeights[i-1]-maxHeights[i])
#         # while maxHeights[i]<maxHeights[i-1]:
#         #     maxHeights[i-1]-=1
#         #     add-=1
# for i in range(ind,n-1):
#     print(maxHeights[i])
#     if maxHeights[i]<maxHeights[i+1]:
#         maxHeights[i+1] -= (maxHeights[i+1]-maxHeights[i])
        # add -= (maxHeights[i+1]-maxHeights[i])
        # while maxHeights[i]<maxHeights[i+1]:
        #     maxHeights[i+1]-=1
        #     add-=1
# for j in range(n):
#     val=0
#     end=maxi
#     for i in range(j,n):
#         if maxHeights[i]>=end:
#             val+=end
#         else:
#             end=maxHeights[i]
#             val+=maxHeights[i]
#     end=maxi
#     for i in range(j-1,0,-1):
#         if maxHeights[i]>=end:
#             val+=end
#         else:
#             end+=maxHeights[i]
#             val+=maxHeights[i]
#     ans=max(ans,val)
# print(ans)

n = len(maxHeights)

maxi=max(maxHeights)
ans = 0

for j in range(n):
    val = 0
    end = maxi

    for i in range(j, n):
        if maxHeights[i] >= end:
            val += end
        else:
            end = maxHeights[i]
            val += maxHeights[i]

    end = maxi

    for i in range(j - 1, -1, -1):
        if maxHeights[i] >= end:
            val += end
        else:
            end = maxHeights[i]
            val += maxHeights[i]

    ans = max(ans, val)
print(ans)
# return ans
