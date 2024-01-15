import math
for i in range(int(input())):
    a, b = map(int, input().split())
    print(round(math.sqrt(2*(a-b))))
