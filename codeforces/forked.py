import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    xk,yk=map(int,input().split())
    xq,yq=map(int,input().split())
    d1={(xq - a, yq - b), (xq - b, yq - a), (xq + a, yq + b), (xq + b, yq + a),
        (xq - a, yq + b), (xq + b, yq - a), (xq + a, yq - b), (xq - b, yq + a)}
    d2={(xk - a, yk - b), (xk - b, yk - a), (xk + a, yk + b), (xk + b, yk + a),
        (xk - a, yk + b), (xk + b, yk - a), (xk + a, yk - b), (xk - b, yk + a)}
    print(sum(1 for i in d1 if i in d2))
for _ in range(int(input())):
   main()