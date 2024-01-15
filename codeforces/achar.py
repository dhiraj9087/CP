# for i in range((int(input()))):
#     n,k=map(int,input().split())
#     a=[1]*n
#     print(a)
#     c=0
#     for i in range(len(a)-1):
#         if a[i]*a[i+1]==1:
#             c+=1
#     print(c)
    # if c>k:
    #     for i in range(len(a)):
    #         a[i]=-1
def find_array_with_characteristic(n, k):
    arr = [1] * n
    pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] * arr[j] == 1:
                pairs += 1

    while pairs > k:
        for i in range(n):
            if pairs == k:
                break
            if arr[i] == 1:
                arr[i] = -1
                pairs -= i

    return arr
for i in range((int(input()))):
    n,k=map(int,input().split())
    print(find_array_with_characteristic(n,k))
    