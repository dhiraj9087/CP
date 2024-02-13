import math
import sys
input=sys.stdin.readline
def reverse_digits(num):
        return int(str(num)[::-1])
def main():
    n,m=map(int,input().split())
    nums=list(map(int,input().split()))
    while len(nums) > 1:
        # Anna's turn
        num = max(nums)
        if num < 10**m:
            return "Anna"
        nums.remove(num)
        nums.append(reverse_digits(num))
        
        # Sasha's turn
        num1 = nums.pop()
        num2 = nums.pop()
        nums.append(int(str(num1) + str(num2)) if num1 < num2 else int(str(num2) + str(num1)))
        
        # Only one number left
    print("Sasha" if nums[0] >= 10**m else "Anna")
for _ in range(int(input())):
   main()