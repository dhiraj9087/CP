import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    one=s.count('1')
    max_length = 0
    current_length = 0
    for char in s:
        if char == '0':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    print(max_length+one)

for _ in range(int(input())):
   main()