import math
import sys
input=sys.stdin.readline
mod=10**9 + 7
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
# def sum_of_series(a,r,k):
#     # a = 12 
#     # r = 2  
#     n = k   

#     series_sum = a * ((r**n) - 1) // (r - 1)
#     return series_sum
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    maxi=max_subarray_sum(a)
    # print(maxi)
    total=sum(a)
    if maxi<=0:
        print(total%mod)
        return
    else:
        # ans=sum_of_series(maxi,2,k)
        # ans=maxi
        # add=ans
        # while k>1:
        #     ans*=2
        #     add+=ans
        #     k-=1
        # print((add+total)%mod)
        ans = (maxi * ((2**k) - 1)) % mod
        add = ans 
        result = (add + total) % mod
        print(result)
        return
        

for _ in range(int(input())):
   main()