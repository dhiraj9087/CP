import math
import sys
input=sys.stdin.readline
def main():
    x, y, z = map(int, input().split())
    g = math.gcd(x, y)
    if z == 1:
        print(min(x, y) + g)
    else:
        print(2 * g)
    # print(math.gcd(1,5),math.lcm(1,5))
for _ in range(int(input())):
   main()