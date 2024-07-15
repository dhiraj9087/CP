start=10
goal=7
num = start^goal
ans=0
for i in range(32):
    if num & (1<<i)!=0:
        ans+=1
print(ans)