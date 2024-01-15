import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    v = []
    arr=[]
    for _ in range(n):
        a, b = map(int, input().split())
        v.append((a, b))
        
    v.sort()
    for i,j in v:
        arr.append(j)
    # print(arr)
    ans=0
    def count_inversions(arr):
        if len(arr) <= 1:
            return 0, arr

        mid = len(arr) // 2
        left_count, left = count_inversions(arr[:mid])
        right_count, right = count_inversions(arr[mid:])
        merge_count, merged = merge_and_count(left, right)

        total_count = left_count + right_count + merge_count

        return total_count, merged

    def merge_and_count(left, right):
        i = j = 0
        count = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return count, merged
    ans, _ = count_inversions(arr)
    print(ans)
    
for _ in range(int(input())):
   main()