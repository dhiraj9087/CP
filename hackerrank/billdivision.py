n,k=map(int,input().split())
bill=list(map(int,input().split()))
b=int(input())
bill.pop(k)
#print(bill)
due=sum(bill)//2
print(b-due)