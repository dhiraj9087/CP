def main():
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]]+=1
        else:
            d[a[i]]=1
    print(max(d.values()),len(set(a)))
main()
