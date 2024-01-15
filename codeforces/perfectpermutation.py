n=int(input())
numbers=[]
for i in range(1,n+1):
    numbers.append(i)
#print(numbers)
if(n%2!=0):
    print("-1")
else:
    for i in range(0,len(numbers) - 1,2):
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    for i in numbers:
        print(i,end=' ')

    