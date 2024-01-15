# a=int(input())
# a=str(a)
# a1=a.count('1')
# a14=a.count('14')
# a144=a.count('144')
# c=0
# for i in range(len(a)):
#     if a[i]=='1' or a[i:i+2:]=='14' or a[i:i+3:]=='144':
#         c+=1
#         print(a[i],a[i:i+2:],a[i:i+3:])
# #print(c)
# if a1==len(a) or a14==len(a)//2 or a144==len(a)//3:
#     print("YES")
# elif c==a1+a14+a144:
#     print("NO")

# else:
#     print("YES")
#print(a1,a14,a144)
# print(a[1:3:])
num = input()
while num:
    if num.startswith('144'):
        num = num[3:]
    elif num.startswith('14'):
        num = num[2:]
    elif num.startswith('1'):
        num = num[1:]
    else:
        print("NO")
        break
else:
    print("YES")
