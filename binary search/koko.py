import math
piles = [3,6,7,11]
h=8
def time(piles,k):
            c=0
            for i in range(len(piles)):
                c+=(math.ceil(piles[i]/k))
            return c

low,high=1,max(piles)
ans=float('inf')
while low<=high:
    mid = (low+high) // 2
    t=time(piles,mid)
    if t>h:
        low=mid+1
    else:
        ans=min(ans,mid)
        high=mid-1
# print(low,high,mid,ans)
print(ans)