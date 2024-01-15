import math
import sys
input=sys.stdin.readline
def checkPalindromenumber(n):
   reverse = 0
   temp = n
   while temp != 0:
      reverse = (reverse * 10) + (temp % 10)
      temp = temp // 10
   return reverse == n

def primenum(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [x for x in range(limit + 1) if primes[x]]


def main():
   n=int(input())
   if n<=4:
      print(0,n)
      return
   print(1,n-1)
   # rng=10**5
   # pr=primenum(rng)
   # # print(pr)
   # ans=[]
   # i=0
   # even,odd=0,0
   # while len(ans)<n:
   #    if checkPalindromenumber(pr[i]):
   #       ans.append(pr[i])
   #       if len(str(pr[i]))%2==0:
   #          even+=1
   #       else:
   #          odd+=1
   #    i+=1
   # print(ans)
for _ in range(int(input())):
   main()