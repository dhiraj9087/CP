# cook your dish here
for i in range((int(input()))):
    n=int(input())
    s=input()
    a=s.count('1')
    b=s.count('0')
    if(a==b):
        print(a)
    elif(a>b):
        print(b+1)
    else:
        print(a)