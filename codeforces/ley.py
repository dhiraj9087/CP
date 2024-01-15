import math
import sys
input=sys.stdin.readline
def main():
    a=input().strip()
    b=input().strip()
    c=input().strip()
    if '?' in a:
        if 'A' not in a:
            print('A')
            return
        if 'B' not in a:
            print('B')
            return
        print('C')
        return
    if '?' in b:
        if 'A' not in b:
            print('A')
            return
        if 'B' not in b:
            print('B')
            return
        print('C')
        return
    if '?' in c:
        if 'A' not in c:
            print('A')
            return
        if 'B' not in c:
            print('B')
            return
        print('C')
        return
    
for _ in range(int(input())):
   main()