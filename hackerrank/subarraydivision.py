n = int(input().strip())
s = list(map(int, input().rstrip().split()))
d,m=map(int,input().split())
q=0
if(len(s)==1):
    for i in range(len(s)):
        a=s[i:m+i]
        # if(sum(d)==d):
        #     q+=1
        #print(sum(d))
        w=sum(a)
        if(w==d):
            q+=1
else:
    for i in range(len(s)-1):
            a=s[i:m+i]
            # if(sum(d)==d):
            #     q+=1
            #print(sum(d))
            w=sum(a)
            if(w==d):
                q+=1
print(q)
