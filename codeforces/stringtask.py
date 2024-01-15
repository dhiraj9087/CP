s=input()
s=s.lower()
a='aoyeui'
q=''
for i in range(len(s)):
    if s[i] not in a:
        q=q+s[i].lower()
    # if s[i]
for i in q:
    print('.',end='')
    print(i,end='')
# print(q)