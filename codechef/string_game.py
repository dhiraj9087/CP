# cook your dish here
y=int(input())
for i in range(y):
    n=int(input())
    s=input()
    s=list(s)
    for i in set(s):
        c=s.count(i)
        if (c%2!=0):
            print("NO")
            break
    else:
        print("YES")