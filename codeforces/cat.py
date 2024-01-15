from collections import OrderedDict
for i in range((int(input()))):
    n=int(input())
    s=input()
    a=s.lower()
    u1 = list(OrderedDict.fromkeys(a))
    u2= ''.join(u1)
    #print(u2)
    if(a=='meowmeow' or a=='meowmeo' or a=='meowme' or a=='meowm' ):
        print("NO")
    elif(u2=='meow'):
        print("YES")
    else:
        print("NO")
    #print(u2)
    #print(a)
    # c=0
    # for i in a:
    #     if(i!='m' or i!='e' or i!='o' or i!='w'):
    #         a.pop(i)
    # print(a)
    # m=(a.find('m'))
    # e=(a.find('e'))
    # o=(a.find('o'))
    # w=(a.find('w'))
    # if(m<e and e<o and o<w):
    #     print("YES")
    # else:
    #     print("NO")
    

    
    


