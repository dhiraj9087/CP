y=int(input())
for i in range(y):
    n=int(input())
    s=input('')
    q=[]
    w=[]
    for i in range(len(s)):
        if(s[i]=='1'):
            q.append(i)
    #print(q)
    for i in range((len(q)-1)):
        a=q[i+1]-q[i]
        w.append(a)
    #print(w)
    for i in range(len(w)):
        if(w[i]%2==0):
            print('2q')
        elif(w[i]%2!=0):
            print('1e')