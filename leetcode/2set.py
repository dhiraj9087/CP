import math
import sys
input=sys.stdin.readline
def main():
    nums=list(map(int,input().split()))
    g=math.gcd
    print(g(*nums))
    a=[]
    # print(a,b)
# for _ in range(int(input())):
main()