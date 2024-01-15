for i in range((int(input()))):
    n,m=map(int,input().split())
    s1=input()
    s2=input()
    c=0
    f=0
    def check(s):
        for i in range(len(s)-2):
            if(s[i]!=s[i+2]):
                return False
        if(s[0]==s[1]):
            return False
        else:
            return True
    if(check(s1)==True and check(s2)==True):
        print("YES")
    elif(check(s1)==True and s1[len(s1)-1]!=s2[len(s2)-1]  or check(s2)==True and s2[len(s2)-1]!=s1[len(s1)-1]):
        print("YES")
    else:
        print("NO")
    #print(c)