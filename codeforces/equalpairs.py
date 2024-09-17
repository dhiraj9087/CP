import math
import sys
input=sys.stdin.readline
from collections import Counter
def pair(a):
    ans=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                ans+=1
    return ans
def main():
    n=int(input())
    a=list(map(int,input().split()))
    hash_table = [0] * 110
        
    for num in a:
        hash_table[num] += 1
    
    m = 0
    ans = 0
    
    for i in range(1, 101):
        if hash_table[i] > m:
            ans += (m * (m - 1) // 2)
            m = hash_table[i]
        else:
            ans += hash_table[i] * (hash_table[i] - 1) // 2
    
    m += hash_table[0]
    print(int(m * (m - 1) // 2) + ans)
for _ in range(int(input())):
   main()