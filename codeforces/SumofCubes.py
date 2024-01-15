def main():
    x=int(input())
    y=int(x**(1/3))
    l,r=1,y
    while l<=r:
        s=l**3 + r**3
        if s == x:
            print("YES")
            return
        elif s > x:
            r-=1
        else:
            l+=1
    print("NO")
    
        

for _ in range((int(input()))):
    main()