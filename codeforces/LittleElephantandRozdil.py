n=int(input())
a=list(map(int,input().split()))
if a.count(min(a))>1:
    print("Still Rozdil")
else:
    print(a.index(min(a))+1)