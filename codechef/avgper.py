def main():
    n = int(input())
    
    if n==3:
        print("3 2 1")
        return
    a=[0]*n
    a[0]=n-1
    a[n-1]=n
    a[1]=n-2
    a[n-2]=n-3
    j=1
    for i in range(2,n-2):
        a[i]=j
        j+=1
    print(*a)


        
for _ in range(int(input())):
    main()