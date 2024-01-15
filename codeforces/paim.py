
def palin(a,x):
    i, j = 0, len(a) - 1
    while i < j:
        if a[i] % x != a[j] % x:
            return False
        i += 1
        j -= 1
    return True

def palin2(a):
    max_a = max(a)
    left, right = 1, max_a
    while left <= right:
        if palin(a, max_a)==False:
            max_a-=1
            right-=1
        else:
            return right
        
    return right


# def palin(x):
#     i,j=0,len(a)-1
#     while i<j:
#         if a[i] % x != a[j] % x:
#             return False
#         i+=1
#         j-=1
#     return x


for i in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    # x=min(a)
    # if x==0:
    #     x+=1
    # if palin(x) == False:
    #     x+=1
    # print(palin(x))
    print(palin2(a))