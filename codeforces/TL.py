n,m=map(int,input().split())
a,b=list(map(int,input().split())),list(map(int,input().split()))
q=min(a)
w=min(b)
if q*2>=w:
    print("-1")
elif max(a)>=min(b):
    print('-1')
else:
    if q*2 < max(a):
        print(max(a))
    else:
        print(q*2)
