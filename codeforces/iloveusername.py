n = int(input())
arr = list(map(int, input().split()))
amazing = 0
a = arr[0]
for m in range(1, n):
    if arr[m] > a:
        a = arr[m]
        amazing += 1
a = arr[0]
for m in range(1, n):
    if arr[m] < a:
        a= arr[m]
        amazing += 1
print(amazing)
