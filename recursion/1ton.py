def fun(a,n):
    if a==n:
        return
    print(a)
    a+=1
    fun(a,n)
n=int(input())
fun(0,n+1)