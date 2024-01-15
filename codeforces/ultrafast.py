s1=str((input()))
s2=str((input()))
# s3=str(s1)
# s4=str(s2)
s=[]
str=""
for i in range(len(s1)):
    if s1[i]==s2[i]:
        s.append(0)
    else:
        s.append(1)
for i in range(len(s)):
    print(s[i],end='')
