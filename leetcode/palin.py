# def sub(s):
s=input()
a=""
al=0
if len(s)%2!=0:
    for i in range(len(s)):
        # ptr=len(s)//2
        lptr,rptr=i,i
        while lptr>=0 and rptr<len(s) and s[lptr]==s[rptr]:
            if rptr-lptr+1>al:
                a=s[lptr:rptr+1:]
                al=rptr - lptr +1
            lptr -=1
            rptr+=1
            # print(lptr,rptr)

    print(a)
else:
    for i in range(len(s)):
        lptr,rptr=i,i+1
        while lptr>=0 and rptr<len(s) and s[lptr]==s[rptr]:
            if rptr-lptr+1>al:
                a=s[lptr:rptr+1:]
                al=rptr - lptr +1
            lptr -=1
            rptr+=1
    print(a)
