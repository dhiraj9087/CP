def fun(a,n,add):
    if a>n:
        # print(add)
        return add
    add+=a
    return fun(a+1,n,add)
    # return add

n=int(input())
add=0
# fun(1,n,add) 
print(fun(1,n,add) )