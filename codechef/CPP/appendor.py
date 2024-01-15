# for i in range((int(input()))):
#     n,y=map(int,input().split())
#     a = list(map(int,input().split()))
#     c=0
#     for i in range(len(a)):
# 	    c=c|a[i]
#     print(y-c)
#     #print(c)



a = list(map(int,input().split()))
c=0
for i in range(len(a)):
	c=c^a[i]

print(c)
