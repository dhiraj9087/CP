import math
import sys
input=sys.stdin.readline


def main():
    s=input().strip()
    if len((s))==1:
        print(s+'a' if 'a' not in s else s+'b')
        return
    ind=-1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            ind=i+1
            break
    if ind==-1:
        print(s+alphabet[(alphabet.index(s[ind])+1)%26])
        return
    print(s[0:ind] + alphabet[(alphabet.index(s[ind])+1)%26] + s[ind::])
for _ in range(int(input())):
   main()