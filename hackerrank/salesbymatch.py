n = int(input().strip())

ar = list(map(int, input().rstrip().split()))
s=[]
# for i in range(len(ar)):
#         # if(ar.count(ar[i])%2==0):
#         #     s=s+1
#         print(ar.count(ar[i]))
se=list(set(ar))
#print(se)
fr=[]

for i in range(len(se)):
    fr.append(ar.count(se[i]))
#print(fr)
for i in range(len(fr)):
    if fr[i]>=2:
        if(fr[i]%2==0):
            s.append(fr[i]//2)
        else:
            s.append((fr[i]-1)//2)
print(sum(s))