import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    v = [n // 5] * 5
    vow = 'aeiou'
    for i in range(n % 5):
        v[i] += 1
    
    result = ''.join(vow[i] * v[i] for i in range(5))
    print(result)
for _ in range(int(input())):
   main()