import math
for i in range((int(input()))):
    n=int(input())
    lst=list(map(int,input().split()))
    #print(math.gcd(lst[0],lst[1]))
    q=[math.gcd(lst[0],lst[1])]
    g=math.gcd(lst[0],lst[1])
    if(n>2):
        for i in range(2,n):
            g=math.gcd(g,lst[i])
            q.append(g)

        #q.append(lst[1+i])
    #else:
        #q.append(g)
    print(q)
    if(min(q)<n):
        print("Yes")
    else:
        print("No")