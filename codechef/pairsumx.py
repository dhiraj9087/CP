import math
import sys
input=sys.stdin.readline
from collections import defaultdict
def count_digits(num):
    if num == 0:
        return 1
    return math.floor(math.log10(num) + 1)

def find_pairs_with_sum_digits(arr, X):
    
    count_map = defaultdict(int)
    result = 0
    
    for num in arr:
        target_sum_digits = X
        for key in count_map:
            if count_digits(num + key) == target_sum_digits:
                result += count_map[key]
        
        count_map[num] += 1
    # print(count_map)
    return result
def main():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    ans = find_pairs_with_sum_digits(a, x)
    print(ans)
    if ans==0:
        print(0)
        return
    if ans==1:
        print(2)
        return
    


    

for _ in range(int(input())):
   main()