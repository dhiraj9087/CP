# cook your dish here
y=int(input())
for i in range(y):
    lst = []
    n=int(input())
    for i in range(0, n):
	    ele = input()

	    lst.append(ele) 
	
    lst.sort()
    print(lst)
    a=len(lst)
    
    print(a)
    print(lst[a-1])