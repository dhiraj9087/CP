import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    s=input().strip()
    t=input().strip()
    if len(set(s))==1 and s[0]=='?':
        print("YES")
        print(t+'a'*len(s[:len(s)-len(t)]))
        return
    c=s.count('?')
    if c==1 and len(t)==1:
        print("YES")
        ind=s.index('?')
        print(s[:ind]+t+s[ind+1:])
        return
    s=list(s)
    i,j=0,0
    while i<len(s) and j<len(t):
        if s[i]==t[j] or s[i]=='?':
            s[i]=t[j]
            i+=1
            j+=1
        else:
            i+=1
    if j!=len(t):
        print("NO")
        return
    while i<len(s):
        if s[i]=='?':
            s[i]='a'
        i+=1
    print("YES")
    print(''.join(s))
for _ in range(int(input())):
   main()