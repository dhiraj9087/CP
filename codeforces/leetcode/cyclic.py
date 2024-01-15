# str1 = "abc"
# str2 = "ad"
str1 = "zc"
str2 = "ad"
"eao"
"ofa" 
# a=[ord(i) for i in str1]
# a=[]
# for i in str1:
#     # a.append(ord(i))
#     if ord(i)==122:
#         a.append(97)
#     else:
#         a.append(ord(i))
# print(a)
c=0
# index=0
# for i in str2:
#     # ind=str1.find(i,index) or str1.find(chr(ord(i)-1),index)
     
#     if ind==-1:
#         print("NO")
#     else:
#         index+=1
#         c+=1
# print(c)
# return True if c==len(str2) else False
n1,n2=len(str1),len(str2)
l,r = 0, 0  
while l < n1 and r < n2:
    if str1[l]==str2[r] or ord(str1[l])+1==ord(str2[r]) or (ord(str1[l])==122 and ord(str2[r])==97):
        l+=1
        r+=1
        c+=1
    else:
        l+=1
print(c)


