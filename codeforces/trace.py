import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a = list(map(int, input().split()))
    arr = [0] * 26
    res = ""
    for i in a:
        for j in range(26):
            if arr[j] == i:
                res += chr(97 + j)
                arr[j] += 1
                break
    print(res)
for _ in range(int(input())):
   main()