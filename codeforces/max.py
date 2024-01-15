def main():
    a,b=map(str,input().split())
    if len(a)<len(b):
        a='0'*(len(b)-len(a)) + a
    ans=0
    for i in range(len(b)):
        if ans:
            ans += 9
        else:
            ans += abs(ord(a[i]) - ord(b[i]))
            

    print(ans)
for _ in range(int(input())):
    main()