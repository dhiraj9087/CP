for i in range((int(input()))):
    s=input()
    a=[]
    for i in str(s):
        a.append(int(i))
    print(a)
    counter = 0
    num = a[0]
    for i in a:
        curr_frequency = a.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    z=(a.count(num))
    if z<=2:
        print("4")
    elif z==3:
        print("6")
    else:
        print("-1")
    


    