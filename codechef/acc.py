import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    for k in range(m):
        s=input().strip()
        if len(s)!=n:
            print("NO")
            break
        else:
            d={}
            arr=[]
            for i in range(len(s)):
                if s[i] in d:
                    if d[s[i]]!=a[i]:
                        print("NO")
                        break
                else:
                    d[s[i]]=a[i]
                    arr.append(a[i])
            else:
                arr.sort()
                for i in range(1,len(arr)):
                    if arr[i]==a[i-1]:
                        print("NO","see")
                        break
                else:
                    print("YES")
             


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime
for _ in range(int(input())):
#    arr=sieve_of_eratosthenes(201)
   main()



# for q in range(int(input())):
#     n=int(input())
#     a=list(map(int,input().split(' ')))
#     m=int(input())
#     for w in range(m):
#         s=input()
#         if(len(s)!=n):
#             print("NO")
#         else:
#             d={}
#             l=[]
#             for i in range(len(s)):
#                 if(s[i] in d):
#                     if(d[s[i]]!=a[i]):
#                         print("NO")
#                         break
#                 else:
#                     d[s[i]]=a[i]
#                     l.append(a[i])
#             else:
#                 l.sort()
#                 for i in range(1,len(l)):
#                     if(l[i]==l[i-1]):
#                         print("NO")
#                         break
#                 else:
#                     print("YES")            
