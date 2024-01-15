
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)



#above code by using comprihensation

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if "a" in x]


print(newlist)






fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x.upper() for x in fruits]
print(newlist)







fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)





fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]     #replace

print(newlist)
