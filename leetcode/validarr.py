import math
import sys
input=sys.stdin.readline
def main():
    for i in range(len(nums)):
        if nums[i] + nums[i+1]>=m:
            return True
    return False

    
        

    

for _ in range(int(input())):
    nums = [2, 2 ,1]
    m = 4
    nums = [2, 1, 3]
    m = 5 
    nums = [2, 3, 3, 2, 3]
    m = 6
    main()