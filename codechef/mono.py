for i in range((int(input()))):
    a,b,c,d=map(int,input().split())
    l=[a,b,c,d]
    m=max(l)
    l.remove(m)
    if m>sum(l): print("YES")
    else:print("NO")