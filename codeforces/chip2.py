s = "aaabbbcc"
# s.sort()
def fact(n):
    if n==0:
        return 1
    a=fact(n-1)*n
    return a

print(fact(5))
# fact(5)