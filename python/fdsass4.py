dic = { }
while True :
    name = input( "Enter name of friend :-")
    phone = int( input("Enter phone number of friend :-" ))
    dic [name] = phone
    choise = input("Enter Q to quit otherwise N :-")
    if choise == "Q" or choise == "q" :
        break

#a
print()
print("a :-")
print(dic)

#b
print()
print("b :-")
name = input( "Enter name of friend :-")
phone = int(input("Enter phone number of friend :-" ))
dic [name] = phone
print(dic)

#c
print()
print("c :-")
name = input( "Enter name of that friend which you want to delete :-")
del dic[ name ]
print(dic)

#d
print()
print("d :-")
name = input( "Enter name of that friend which you want to change his phone number :-")
phone = int(input ("Enter phone number of friend :-" ))
del dic [ name]
dic[ name ] = phone
print(dic)

#e
print()
print("e :-")
name = input( "Enter name of that friend which you want to search :-")
if name in dic :
    print(" Found")
else :
    print( "Not Found ")

#f
print()
print("f :-")
newdic = {}
key = list( dic.keys())
key.sort()
for i in key :
    newdic [ i ] = dic [ i ]
print(newdic)