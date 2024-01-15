for _ in range((int(input()))):
    n=int(input())
    s=input()
    c=0
    if len(set(s))==1:
        print("Ramos")
    else:
        for i in range(0,n-1,2):
            if s[i]!=s[i+1]:
                c+=1
        print(c)
        if c%2!=0:
            print("Zlatan")
        else:
            print("Ramos")
