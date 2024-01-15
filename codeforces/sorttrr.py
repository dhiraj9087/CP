import math
import sys
from collections import Counter
input=sys.stdin.readline
def main():
    word = "igigee"  #igig, ee, igigee
    k = 2
    # word = "aaabbbccc"  #aaa, bbb, ccc, aaabbb, bbbccc, aaabbbccc.
    # k = 3
    d=Counter(word)
    print(d)
    
# for _ in range(int(input())):
main()