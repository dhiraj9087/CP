def knapsack(w,weight,profit,n):
    if n==0 or w==0:
        return 0
    if weight[n-1]>w:
        return knapsack(w,weight,profit,n-1)
    else:
        return max(profit[n-1]+knapsack(w-weight[n-1],weight,profit,n-1),knapsack(w,weight,profit,n-1))






n,w=map(int,input().split())
profit=list(map(int,input().split()))
weight=list(map(int,input().split()))
print(knapsack(w,weight,profit,n))