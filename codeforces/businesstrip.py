n=int(input())
a=list(map(int,input().split()))
a.sort()
#print(a[::-1])
a=a[::-1]
s=0
for i in range(len(a)):
    s+=a[i]
    #print(s)
    if n==0:
        print("0")
        break
    if s==n:
        print(i+1)
        break
    elif s>n:
        print(i+1)
        break
else:
    print("-1")
        