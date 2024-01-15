S=input()
a=" "

for x in S:
    if(x.lower()=="a" or x.lower()=="e" or x.lower()=="i" or x.lower()=="o" or x.lower()=="u"):
        a=a+"*"
    else:
        a=a+x
print(S,end=" ")