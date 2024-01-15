s=input()
c=0
for i in range(len(s)):
    if(ord(s[i])>=65 and ord(s[i])<=90 ):
        c+=1
        print(s[i])
print(c+1)