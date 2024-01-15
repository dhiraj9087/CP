for i in range((int(input()))):
    s=input()
    day=int(s[0:2])
    month=int(s[3:5])
    # print(day,month)
    if day>12 and month<=12:
        print("DD/MM/YYYY")
    elif day<=12 and month<=12:
        print("BOTH")
    else:
        print("MM/DD/YYYY")