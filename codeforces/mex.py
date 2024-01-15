import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    min_a = min(a)
    operation_count = 0
    i=0
    # Simulate the process
    while operation_count < k:
        if min_a not in a[i::]:
            break
        operation_count += 1
        min_a += 1
        i+=1
    
    # Apply operations to the array
    updated_array = [min_a + operation_count for _ in range(n)]
    
    print(*updated_array) 
for _ in range(int(input())):
   main()