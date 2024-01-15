for i in range((int(input()))):
    a=[]
    count=0
    s=input()
    for i in s:
        a.append(int(i))
    #r=list(int(a))
    #print(a)
    s=int(s)
    for i in range(len(a)):
        if(a[i]==0):
            pass
        elif(s%a[i]==0):
            count+=1
    print(count)