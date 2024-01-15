# import itertools
# for i in range((int(input()))):
#     n, q = map(int, input().split())
#     arr = list(map(int,input().split()))
#     pres = list(itertools.accumulate(arr, initial=0))
#     # print(pres)
#     for _ in range(q):
#         l, r, k = map(int, input().split())
#         res = pres[l - 1] + k * (r - l + 1) + pres[-1] - pres[r]
#         # print(pres[l - 1],k * (r - l + 1),pres[-1] ,pres[r])
#         print("YES" if res & 1 else "NO")
    # n,q=map(int,input().split())
    # a=list(map(int,input().split()))
    # old_sum=sum(a)
    # s=0
    # arsum=[0]
    # for i in a:
    #     s+=i
    #     arsum.append(s)
    # # print(arsum)
    # for i in range(q):
    #     # z=list(a)
    #     l,r,k=map(int,input().split())
    #     ans = arsum[l-1] + (k*(r-l+1)) + (arsum[-1] - arsum[r] )
    #     # new_querysum=(r-l+1)*k
    #     # ans = old_sum + new_querysum - new
    #     print("YES" if ans%2!=0 else "NO")
        # new_sum=old_sum-(arsum[r-1]-arsum[l-2]+arsum[l-1] ) +  (r-l+1)*k
       
        # if new_sum%2!=0: print("YES")   
        # else: print("NO")

    
# def STR():
#     n = int(input())
#     q = int(input())
#     a = [0] * n
#     for i in range(n):
#         x = int(input())
#         if i > 0:
#             a[i] = a[i-1] + x
#         else:
#             a[i] = x
#     while q > 0:
#         l, r, k = map(int, input().split())
#         l -= 1
#         r -= 1
#         x = a[r] - a[l-1] if l > 0 else a[r]
#         y = k * (r-l+1)
#         if (sum(a) + y - x) % 2:
#             print("YES")
#         else:
#             print("NO")
#         q -= 1

# import string
# def removeNonAlNum(str):
#     str = ''.join(filter(lambda c: c.isalnum(), str))
#     return str

# def solve():
#     n, q = map(int, input().split())
#     arr = list(map(int, input().split()))
#     a = arr.copy()
#     sum = 0
#     for i in range(n):
#         sum += arr[i]
#     # print(sum)
#     for i in range(1, n):
#         arr[i] = arr[i] + arr[i - 1]
#     print(arr)
#     for i in range(q):
#         l, r, k = map(int, input().split())
#         res = sum - (arr[r - 1] - arr[l - 1] + a[l - 1]) + ((r - l + 1) * k)
#         if res % 2:
#             print("yes")
#         else:
#             print("no")

# t = int(input())
# while t > 0:
#     solve()
#     t -= 1



# for _ in range(int(input())):
#     n, q = map(int, input().split())
#     a = list(map(int, input().split()))
#     total_sum = sum(a)
#     for i in range(q):
#         l, r, k = map(int, input().split())
#         diff = (r - l + 1) * k - (total_sum - sum(a[l-1:r]))
#         print(diff)
#         total_sum += diff
#         a[l-1:r] = [k] * (r - l + 1)
#         if total_sum % 2 != 0:
#             print("YES")
#         else:
#             print("NO")
for i in range((int(input()))):
    n, q = map(int, input().split())
    arr = list(map(int,input().split()))
    # pres = list(itertools.accumulate(arr, initial=0))
    pres=[0]
    curr_sum=0
    for i in arr:
        curr_sum += i
        pres.append(curr_sum)
    pres.append(curr_sum)
    # print(pres)
    for _ in range(q):
        l, r, k = map(int, input().split())
        left_sum = pres[l - 1] 
        mid_sum =  k * (r - l + 1) 
        right_sum= pres[n+1] - pres[r]
        res=left_sum+right_sum+mid_sum
        print("YES" if res & 1 else "NO")

# import sys
# input = sys.stdin.readline

# def solve(n, prefix_arr, l, r, k):
#     sum_left = prefix_arr[l - 1]
#     sum_mid = (r - l + 1) * k
#     sum_right = prefix_arr[n + 1] - prefix_arr[r]
#     if (sum_left + sum_mid + sum_right) % 2 == 1:
#         print("yes")
#     else:
#         print("no")
 
 
# def main():
#     t = int(input())
#     for _ in range(t):
#         n, q = map(int, input().split())
#         arr = list(map(int, input().split()))
#         prefix_arr = [0]
#         curr_sum = 0
#         for i in arr:
#             curr_sum += i
#             prefix_arr.append(curr_sum)
#         prefix_arr.append(curr_sum)
#         print(prefix_arr)
#         for _ in range(q):
#             l, r, k = map(int, input().split())
#             solve(n, prefix_arr, l, r, k)
 
 
# main()
