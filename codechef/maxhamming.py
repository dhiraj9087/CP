import math
import sys
input=sys.stdin.readline
def max_hamming_distance_sum(strings):
    M = len(strings)
    N = len(strings[0])
    
    # Count '0's, '1's, and '?'s for each position
    counts = [{'0': 0, '1': 0, '?': 0} for _ in range(N)]
    for s in strings:
        for i, c in enumerate(s):
            counts[i][c] += 1
    
    total_distance = 0
    for i in range(N):
        zeros = counts[i]['0']
        ones = counts[i]['1']
        questions = counts[i]['?']
        
        # Try all possible ways to distribute the '?'s
        max_diff = 0
        for additional_zeros in range(questions + 1):
            total_zeros = zeros + additional_zeros
            total_ones = ones + (questions - additional_zeros)
            diff = total_zeros * total_ones
            max_diff = max(max_diff, diff)
        
        total_distance += max_diff
    
    return total_distance
def main():
    n,m=map(int,input().split())
    l=[]
    for i in range(m):
        s=input().strip()
        l.append(s)
    print(max_hamming_distance_sum(l))
for _ in range(int(input())):
   main()