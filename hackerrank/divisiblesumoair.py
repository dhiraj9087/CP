n,k= map(int,input().split())
ar = list(map(int, input().rstrip().split()))
s=0
for i in range(n):
        for j in range(i+1,n):
            if(i<j and (ar[i]+ar[j])%k==0):
                s+=1
                #print(ar[i],ar[j])
print(s)