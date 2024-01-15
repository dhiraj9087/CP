def main():
    n=int(input())
    d={}
    for i in range(n):
        a,b=map(int,input().split())
        if (a,b) in d:
            d[(a,b)]+=1
        else:
            d[(a,b)]=1
    print(max(d.values()))
main()
