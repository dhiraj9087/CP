import sys;input=sys.stdin.readline
def main():
    n,m,h=map(int,input().split())
    q=[]
    for i in range(n):
        a=sorted(list(map(int,input().split())))
        s=0
        c=0
        p=0
        while c<m and s+a[c]<=h:
            s+=a[c]
            p+=s
            c+=1
        q.append((-c,p))
    ind = q[0]
    q.sort()
    print(q.index(ind)+1)
    

for _ in range(int(input())):
    main()    
