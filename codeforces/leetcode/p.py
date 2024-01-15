import math
# def isPrime(n):
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def printPrimeFactors(n):
#     if n <= 1:
#         return
#     while n % 2 == 0:
#         print(2, end=" ")
#         n = n // 2

#     while n % 3 == 0:
#         print(3, end=" ")
#         n = n // 3
#     i = 5
#     while i * i <= n:
#         while n % i == 0:
#             print(i, end=" ")
#             n = n // i
#         while n % (i + 2) == 0:
#             print(i + 2, end=" ")
#             n = n // (i + 2)
#         i += 6
#     if n > 3:
#         print(n, end=" ")
#     print()

# # printPrimeFactors(12)
# a=[]
# left,right=4,6
# for i in range(left,right+1):
#     if isPrime(i):
#         a.append(i)
# ans=[0,0]
# mini=float('inf')
# for i in range(1,len(a)):
#     if a[i]-a[i-1]<mini:
#         mini=a[i]-a[i-1]
#         ans[0]=a[i-1]
#         ans[1]=a[i]
# print(a,ans)
def printDivisors(n):
    a=[]
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                a.append(i)
            else:
                a.append(i)
                a.append(n//i)
    return a
print(printDivisors(6))