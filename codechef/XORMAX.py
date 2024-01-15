# cook your dish here
y=int(input())
for i in range(y):
    p=input()
    q=input()
    a=list(p)
    b=list(q)
    c=list()
    #while(a[0]!=b[0]):
    def loop():

        for i in range(len(a)-1):
            if(a[i]==b[i]):
                temp = b[i]
                b[i] = b[i+1]
                b[i+1] = temp
                #print(a)
                #print(b)
    def main():
        loop()
        

        for i in range(len(a)):
            # if(a[0]==b[0]):
            #     #print(a)
            #     #print(b)
            #     loop()
            if(a[i]!=b[i]):
                print("1",end='')
            else:   
                print("0",end='')
        print()
        # if(a[i]==b[i]):
        #     loop()
    main()