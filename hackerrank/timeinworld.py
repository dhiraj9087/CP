h=int(input())
m=int(input())
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
w=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","quater","sixteen","seventeen","eighteen","ninteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","half"]
for i in range(len(n)):
    if(h==n[i]):
        b=w[i]
    if(m==n[i]):
        c=w[i]
#print(b)
if(m<=30):
    if(m==00):
        print(b,"o' clock")
    elif(m==15):
        print("quarter past",b)
    elif(m==30):
        print("half past",b)
    else:
        if(m==1):
            print(c,"minute past", b)
        else:
            print(c,"minutes past", b)
elif(m>30):
    c=60-m
    for i in range(len(n)):
        if(c==n[i]):
            r=w[i]
        if(h==n[i]):
            if(h==12):
                f=w[0]
            else:
                f=w[i+1]
            #print(f)
    if(c==00):
        print(r,"o' clock")
    elif(c==15):
        print("quarter to",f)
    else:
        if(c==1):
            print(r,"minute to",f)
        else:
            print(r,"minutes to",f)