s=input()
a=int(input())
q=[]
if(a%len(s)==0):
    print((a//len(s))*s.count('a'))
else:
#print(11/3)
    for i in range(a-(a//len(s))*len(s)):
        q.append(s[i])
    print((a//len(s))*s.count('a')+q.count('a'))
