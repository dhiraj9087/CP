n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
mp1,mp2={},{}
for i in range(0,n):
    mp1[l1[i]]=i+1
    mp2[l1[i]]=n-i
print(mp1,mp2)
sum1, sum2 = 0, 0
for i in range(len(l2)):
    sum1 += mp1[l2[i]]
    sum2 += mp2[l2[i]]
print(sum1, sum2)
