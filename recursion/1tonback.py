
def fun(a,n):
    if a<1:
        return
    fun(a-1,n)
    print(a)
    # a+=1
    # fun(a,n)
n=int(input())
fun(n,n)