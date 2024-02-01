import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    n,q=map(int,input().split())
    s = input().strip()
    count = 1
    max_length = 0
    lengths = []
    for i in range(1, n):
        if s[i] != s[i - 1]:
            max_length = max(max_length, count)
            count = 1
        else:
            count += 1
    max_length = max(max_length, count)
    lengths.append(max_length)
    index = n
    temp = q
    while temp > 0:
        new_char = input().strip()
        s += new_char
        if s[index] == s[index - 1]:
            count += 1
        else:
            count = 1
        max_length = max(max_length, count)
        lengths.append(max_length)
        index += 1
        temp -= 1
    print(" ".join(map(str, lengths)))

for _ in range(int(input())):
   main()