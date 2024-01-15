import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    word=input().strip()
    # C='bcd'
    # V='ae'
    # for i in range(n):
    vowels = {'a', 'e'}
    consonants = {'b', 'c', 'd'}

    ans = []
    s = ""

    for char in word:
        if s == "":
            s += char
        else:
            if s[-1] in vowels and char in consonants:
                ans.append(s)
                s= char
            elif s[-1] in consonants and char in vowels:
                s+= char
            else:
                ans.append(s)
                s = char

    if s:
        ans.append(s)
    for i in range(1, len(ans)):
        if len(ans[i]) == 1:
            ans[i - 1] += ans[i]
    ans= [i for i in ans if len(i) > 1]

    print('.'.join(ans))
    
for _ in range(int(input())):
   main()