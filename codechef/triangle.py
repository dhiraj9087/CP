import math
import sys
input=sys.stdin.readline
def f(A):
    N = len(A)
    A.sort()  # Sort the array in ascending order
    
    count = 0
    right = 0
    
    for left in range(N - 2):
        while right < N - 1 and A[left] + A[left + 1] > A[right + 1]:
            right += 1
        
        count += (right - left) * (right - left - 1) // 2
    
    return count

def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans = f(a)
    print(ans)
for _ in range(int(input())):
   main()