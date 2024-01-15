from collections import defaultdict
import math
import sys
input=sys.stdin.readline

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def main():
    n=int(input())
    # a=[i for i in range(1,n+1)]
    # a=list(map(int,input().split()))
    # a=[1,2,4,3,6,5,7]
    # # # d=[math.gcd(a[i],a[(i+1)%(n)+1]) for i in range(1,n)]
    # d=[]
    # for i in range(len(a)-1):
    #     q=math.gcd(a[i],a[i%n+1])
    #     d.append(q)
    # print(d)
    # if n%2==0:
    #     for i in range(1,n//2 ):
    #         d.append(i)
    # else:
    #     for i in range(1,n//2+1 ):
    #         d.append(i)
    # print(d)
    # for i in range(n//2):
    # p=[]
    # np=[]
    # for i in range(1,n+1):
    #     if isPrime(i):
    #         p.append(i)
    #     else:
    #         np.append(i)
    # # print(p,np)
    # a=[]
    # if len(p)>len(np):
    #     for i in range(min(len(p),len(np))):
    #         a.append(np[i])
    #         a.append(p[i])
    #     for i in range(len(p)):
    #         if p[i] not in a:
    #             a.append(p[i])
    # else:
    #     for i in range(min(len(p),len(np))):
    #         a.append(np[i])
    #         a.append(p[i])
    #     for i in range(len(np)):
    #         if np[i] not in a:
    #             a.append(np[i])
    # print(*a)
    # if n==5:
    #     print('1 2 4 3 5')
    #     return
    # if n==2:
    #     print('1 2')
    #     return
    
    # a=[i for i in range(1,n+1)]
    # d=[1,2,3]
    # for i in range(1,len(a)):
    #     if 2*a[i] in a:
    #         d.append(2*a[i])
    # for i in a:
    #     if i not in d:
    #         d.append(i)
    # print(d)
    ans = [1] 
    v = [0] * (n + 1) 
    for i in range(2, n + 1):
        if(not v[i]):
            j = i 
            while(j <= n):
                ans.append(j) 
                v[j] = 1 
                j *= 2
    print(*ans)
for _ in range(int(input())):
    main()



