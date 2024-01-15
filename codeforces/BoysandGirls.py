import sys
n,m=map(int,input().split())


sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
s=['B']*n
for i in range(n):
    if s[i]=='B':
        s.insert(i+1,'G')
        m-=1
while m!=0:
    s.append("G")
    m-=1
for i in s:
    print(i,end='')
# print(s)
    