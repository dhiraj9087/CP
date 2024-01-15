y=int(input())
for i in range(y):
    n=int(input())
    s=input()
    s1=input()
    s2=input()
    a=len(s)
    for i in range((a/2)+1):
        s1+=s[i]
    for i in range((a/2),a):
        s2+=s[i]
    if((s1+s2)==(s2+s1)):
        print("YES")
    else:
        print("NO")