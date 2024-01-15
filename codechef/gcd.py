import math
for i in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    w=list(map(int,input().split()))
    z=[]
    for i in range(q):
        for j in range(n):
            # gcd=math.gcd(w[i],a[j])
            if a[j]%w[i]:
                z.append(a[j])
                # a.pop(min(w[i],a[j]))
    # z=math.gcd(w[0],a[2])
    print(z)