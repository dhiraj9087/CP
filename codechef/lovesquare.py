# cook your dish here
import math
for i in range((int(input()))):
    X=int(input())
    N = int(math.sqrt(X)) + 1
    while True:
        squares = int(math.sqrt(N))
        cubes = int(N**(1/3))
        F_N = squares - cubes
        if F_N >= X:
            print(N)
        N += 1
    