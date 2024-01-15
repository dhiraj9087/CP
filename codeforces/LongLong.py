def main():
    n=int(input())
    a=list(map(int,input().split()))
    arr=[]
    s=0
    for i in range(n):
        s+=abs(a[i])
        if a[i]!=0:
            arr.append(a[i])
            
    
    group_count = 0
    in_group = False

    for num in arr:
        if num < 0 and not in_group:
            in_group = True
            group_count += 1
        elif num >= 0 and in_group:
            in_group = False

    print(s,group_count)

            


for _ in range(int(input())):
    main()