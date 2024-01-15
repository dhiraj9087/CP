y=int(input())
for i in range(y):
    n=int(input())
    s=input()
    s1=str()
    s2=str()
    a=len(s)
    b=int((a/2)+1)
    c=int(a/2)
    for i in range(0,(b-1)):
        s1+=s[i]
    for i in range(c,a):
        s2+=s[i]
    q=(s1+s2)
    w=(s2+s1)
    if(q==w):
        print("YES")
    else:
        print("NO")