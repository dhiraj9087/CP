import math
import sys
input=sys.stdin.readline
def main():
    a,b,c,d=map(int,input().split())
    wins = 0

    s1, s2 = 0, 0
    if a > c:
        s1 += 1
    elif c > a:
        s2 += 1
    if b > d:
        s1 += 1
    elif d > b:
        s2 += 1
    if s1 > s2:
        wins += 1

    s1, s2 = 0, 0
    if a > d:
        s1 += 1
    elif d > a:
        s2 += 1
    if b > c:
        s1 += 1
    elif c > b:
        s2 += 1
    if s1 > s2:
        wins += 1

    s1, s2 = 0, 0
    if b > c:
        s1 += 1
    elif c > b:
        s2 += 1
    if a > d:
        s1 += 1
    elif d > a:
        s2 += 1
    if s1 > s2:
        wins += 1

    s1, s2 = 0, 0
    if b > d:
        s1 += 1
    elif d > b:
        s2 += 1
    if a > c:
        s1 += 1
    elif c > a:
        s2 += 1
    if s1 > s2:
        wins += 1

    print(wins) 
for _ in range(int(input())):
   main()