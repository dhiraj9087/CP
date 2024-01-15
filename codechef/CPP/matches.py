# cook your dish here
n=[0,1,2,3,4,5,6,7,8,9]
m=[6,2,5,5,4,5,6,3,7,6]
for i in range((int(input()))):
    a,b=map(int,input().split())
    w=[]
    c=a+b
    c=str(c)
    q=list(c)
    #print(q)
    # print(len(n))
    for i in range(len(q)):
        for j in range(len(n)):
            if(n[j]==int(c[i])):
                w.append(m[j])
                
    print(sum(w))
    
            