n=int(input())
l=list(map(int,input().split()))
q=[]
for i in range(1,6):
    #print(i)
    if (sum(l)+i) %(n+1) != 1:
        q.append(i)
print(len(q))
