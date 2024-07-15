def fun(n):
    res=""
    if n==0:
        return '0'
    while n>0:
        if n%2==1:
            res += '1'
        else:
            res += '0'
        n = n//2
    return res[::-1]


print(fun(10))
