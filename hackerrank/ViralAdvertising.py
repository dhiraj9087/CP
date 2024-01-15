# Day Shared Liked Cumulative
# 1      5     2       2
# 2      6     3       5
# 3      9     4       9
# 4     12     6      15
# 5     18     9      24

t=int(input())
d=2
a=[2]
for i in range(t-1):
    #d=d//2
    d=(d*3)//2
    a.append(d)
print(sum(a))