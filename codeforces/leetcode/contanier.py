height = [1,8,6,2,5,4,8,3,7]
# ans=[]
# n=len(height)
# for i in range(n):
#     for j in range(i+1,n):
#         ans.append(min(height[i],height[j])*(j-i))
# print(max(ans))
n = len(height)
l = 0
r = n - 1
maxi = 0

while l < r:
    area = min(height[l], height[r]) * (r - l)
    maxi = max(maxi, area)
    
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(maxi)
