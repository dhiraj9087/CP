n,x=map(int,input().split())
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def next_prime(num):
    next_num = num + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num
if (next_prime(n)==x):
    print("YES")
else:
    print("NO")