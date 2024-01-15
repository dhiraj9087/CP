y, k, n = map(int,input().split())
count = 0
x1 = (n // k) * k - y
x2 = k - (y % k)
while x2 <= x1:
    print(x2,end=" ")
    x2 += k
    count = 1
if count == 0:
    print(-1)
    