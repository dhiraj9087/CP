def solve():
    n=int(input())
    s=input()
    flag=1
    alice,bob=0,0
    for i in range(len(s)):
        if s[i]=='A' and flag==1:
            alice+=1
            flag=1
        elif s[i]=='B' and flag==1:
            flag=0
        elif s[i]=='A' and flag==0:
            flag=1
        elif s[i]=='B' and flag==0:
            bob+=1
            flag=0
    print(alice,bob)
for _ in range((int(input()))):
    solve()