n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    a.append(i/100)
print((sum(a)/n)*100)