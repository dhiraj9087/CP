s1=input()
s2=input()
n=int(input())
c=0
for i in range(min(len(s1),len(s2))):
    if(s1[i]==s2[i]):
        c+=1
    else:
        break

if(len(s1)+len(s2) - (2*c) == n):
    print("Yes")
elif(s1==s2):
    print("Yes")
else:
    print("No")