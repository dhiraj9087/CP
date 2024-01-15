def main():
    a=input()
    b=input()
    c=input()
    s=a+b+c
    if s[0]==s[1]==s[2] and s[0]!='.':
            print(s[0])
    elif s[3]==s[4]==s[5] and s[3]!='.':
            print(s[3])
    elif s[6]==s[7]==s[8] and s[6]!='.':
            print(s[6])
    elif s[0]==s[3]==s[6] and s[0]!='.':
            print(s[0])
    elif s[1]==s[4]==s[7] and s[1]!='.':
            print(s[1])
    elif s[2]==s[5]==s[8] and s[2]!='.':
            print(s[2])
    elif s[0]==s[4]==s[8] and s[0]!='.':
            print(s[0])
    elif s[2]==s[4]==s[6] and s[2]!='.':
            print(s[2])
    else:
        print('DRAW')
        


for _ in range(int(input())):
    main()