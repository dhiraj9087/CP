import math
import sys
input=sys.stdin.readline
def main():
    s=input().strip()
    s=list(s)
    n=len(s)
    l,u=[],[]
    for i in range(n):
        if s[i]=='B':
            s[i]=''
            if u:s[u.pop()]=''
            continue
        if s[i]=='b':
            s[i]=''
            if l:s[l.pop()]=''
            continue
        if 'a'<=s[i]<='z':
            l+=[i]
        else:
            u+=[i]
    print(''.join(s))
for _ in range(int(input())):
   main()