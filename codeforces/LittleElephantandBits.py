s=int(input())
a=str(s)
e=str(s)
q=(int(a,2))
# e=""
# for i in range(q,-1,-1):
#     w=bin(i).replace("0b","")
#     print(w,i)
    # if len(w)==len(a)-1:
    #     print(w)
    #     break
    # print(w)
    # if 
# print((a))
z=0
for i in range(len(a)):
    a=a.replace(a[i],'')
    # print(a)
    w=int(a,2)
    z=max(w,z)
    # print(z)
    a=str(e)
print(bin(z).replace("0b",""))