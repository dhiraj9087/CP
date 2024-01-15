# for _ in range((int(input()))):
#     n,k,d,w=map(int,input().split())
#     a=list(map(int,input().split()))
#     q,sum=[0],0
#     for i in range(n):
#         sum=sum+a[i]
#         q.append(sum)
#     print(q)
import sys
import math
import itertools

def main():
    t = int(input())
    for _ in range(t):
        n, k, d, w = map(int, input().split())
        arr = list(map(int, input().split()))
        cnt = 0
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] - arr[i] - d <= w and j - i < k:
                j += 1
            cnt += 1
            i = j
        print(cnt)

if __name__ == "__main__":
    main()
