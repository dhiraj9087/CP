import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ind=[]
    # for i in range(1,n):
    #     if a[i] < a[i-1]:
    #         for j in range(i,0,-1):
    #             if a[j] >= a[i-1]:
    #                 break
    #             a[j] += a[j-1]

    #             # diff = a[i] - a[i+1]
    #             # mini = min(diff,50)
    #             ind.append((i,i-1))
    #             # a[i] -= mini
    #             # a[i + 1] += mini
    # print(ind)
    maxi_1=max(a)
    ind_maxi_1=a.index(maxi_1)
    maxi_2=float('-inf')
    for i in range(n):
        maxi_2=max(maxi_2,abs(a[i]))
    ind_maxi_2=a.index(maxi_2)
    print(maxi_1,maxi_2)
    while maxi_1<maxi_2:
        maxi_1=maxi_1+maxi_1
        ind.append()

for _ in range(int(input())):
    main()




