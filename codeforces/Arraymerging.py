def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d=[]
    # l,r=0,0
    # while l<n and r<n:
    #     if a[l]!=b[r]:
    #         r+=1
    #     if a[l]==b[]
    i = j = 0
    n =len(a)
    m = len(b)
    c = []
    max_len = 0
    curr_len = 0
    while i < n and j < m:
        if a[i] == b[j]:
            curr_len += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
        if curr_len > max_len:
            max_len = curr_len
        if i < n and j < m and a[i] != b[j]:
            curr_len = 0
    while i < n:
        c.append(a[i])
        i += 1
    while j < m:
        c.append(b[j])
        j += 1
    # return max_len
    print(max_len)
    
for _ in range((int(input()))):
    main()
