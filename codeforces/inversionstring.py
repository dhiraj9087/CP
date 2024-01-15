for i in range((int(input()))):
    n=int(input())
    st=input()
    st=list(st)
    a=""
    c=0
    for i in range(n):
        s=st[i:n:1]
        #print(s)
        for j in range(i,n):
            if(s[j]=="0"):
                #c+=1
                s[j]="1"
            else:
                s[j]="0"
        print(a.join(s))

    # print(c)
        
    # if(flag==1):
    #      print("Yes")
    # else:
    #      print("No")