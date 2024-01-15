numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
n=int(input())
s=input()
c=0
l=0
u=0
sp=0
sum=n
#q=[]
if(n<6):
    print(6-n)
elif(n>=6):
    for i in range(len(s)):
        if (s[i]) in numbers:
            c+=1
            #sum=sum-c
            #q.append(c)
        if s[i] in lower_case:
                l+=1
                #sum=sum-c
                #q.append(l)
        if s[i] in upper_case:
                    u+=1
                    #sum=sum-c
                    #q.append(u)

        if s[i] in special_characters:
                sp+=1
                        #sum=sum-c
                #q.append(sp)
    q=[c,l,u,sp]
    print(q.count(0))