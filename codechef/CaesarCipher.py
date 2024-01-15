def main():
    n=int(input())
    s=input()
    t=input()
    u=input()
    ind=ord(t[0])-ord(s[0])
    # print(ind)
    new=''
    for i in range(n):
        ch=u[i]
        p=chr(((ord(ch)-97+ind)%26)+97)
        new += p
    print(new)
for _ in range(int(input())):
    main()


