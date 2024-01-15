s3=input()
s4=input()
c=0
s1=s3.replace(" ","")
s2=s4.replace(" ","")
for i in s2:
    if s2.count(i)<=s1.count(i):
        c+=1
if c==len(s2):
    print("YES")
else:
    print("NO")
