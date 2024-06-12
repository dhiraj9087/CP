import math
import sys
input=sys.stdin.readline
def main():
    x,y,z,k=map(int,input().split())
    max_positions = 0

    for a in range(1, int(k**(1/3)) + 1):
        if k % a == 0:
            for b in range(1, int(math.sqrt(k // a)) + 1):
                if (k // a) % b == 0:
                    c = k // (a * b)

                    if a <= x and b <= y and c <= z:
                        max_positions = max(max_positions, (x - a + 1) * (y - b + 1) * (z - c + 1))
                    if a <= x and c <= y and b <= z:
                        max_positions = max(max_positions, (x - a + 1) * (y - c + 1) * (z - b + 1))
                    if b <= x and a <= y and c <= z:
                        max_positions = max(max_positions, (x - b + 1) * (y - a + 1) * (z - c + 1))
                    if b <= x and c <= y and a <= z:
                        max_positions = max(max_positions, (x - b + 1) * (y - c + 1) * (z - a + 1))
                    if c <= x and a <= y and b <= z:
                        max_positions = max(max_positions, (x - c + 1) * (y - a + 1) * (z - b + 1))
                    if c <= x and b <= y and a <= z:
                        max_positions = max(max_positions, (x - c + 1) * (y - b + 1) * (z - a + 1))
    print(max_positions)
for _ in range(int(input())):
   main()