y=int(input())
for i in range(y):
    a=(input(""))
    b=(input(""))
    c=list()
    x=0
    y=0
    for i in range(len(a)):
        if(a[i]=='1' and b[i]=='1'):
            x=x+2
        elif(a[i]=='0' and b[i]=='0'):
            y=y+2
        else:
            x=x+1
            y=y+1
    # print(x)
    # print(y)
    for i in range(len(a)):
        if(i<min(x,y)):
            c.append('1')
        else:
            c.append('0')
    d=''.join(map(str,c))
    print(d)
    