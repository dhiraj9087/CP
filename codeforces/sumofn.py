import math
import sys
input=sys.stdin.readline
maxi=10**6 + 2
arr=[0]*maxi
def fun():
   arr[1] = 1
   for i in range(2, maxi):
      if arr[i] == 0:
         arr[i] = i
         for j in range(i * i, maxi, i):
               if arr[j] == 0:
                  arr[j] = i
def main():
   n=int(input())
   p=[]
   fun()
   for i in range(2, maxi):
         if arr[i] == i:
            p.append(i)
   ans=0
   if arr[n]==n:
      for i in p:
         if i>n:
            break
         ans += (i*n)
      print(ans)
      return
   
   for i in p:
      if i>arr[n]:
         break
      ans+=(i*n)
   print(ans)
       
for _ in range(int(input())):
   main()


# import sys
# input = sys.stdin.read

# MAX_LIMIT = 10**6 + 2

# primes = []
# smallest_prime_factor = [0] * MAX_LIMIT

# def calculate_spf():
#     smallest_prime_factor[1] = 1
#     for i in range(2, MAX_LIMIT):
#         if smallest_prime_factor[i] == 0:
#             smallest_prime_factor[i] = i
#             for j in range(i * i, MAX_LIMIT, i):
#                 if smallest_prime_factor[j] == 0:
#                     smallest_prime_factor[j] = i

# def process(k):
#     result = 0
#     if smallest_prime_factor[k] == k:
#         for prime in primes:
#             if prime > k:
#                 break
#             result += prime * k
#     else:
#         for prime in primes:
#             if prime > smallest_prime_factor[k]:
#                 break
#             result += prime * k
#     print(result)

# def main():
#     calculate_spf()
#     for i in range(2, MAX_LIMIT):
#         if smallest_prime_factor[i] == i:
#             primes.append(i)

#     input_data = input().split()
#     t = int(input_data[0])
#     queries = map(int, input_data[1:t + 1])
#     for k in queries:
#         process(k)

# if __name__ == "__main__":
#     main()
