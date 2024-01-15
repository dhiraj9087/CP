import math
import sys
input=sys.stdin.readline
def main():
    # a=input()
    # if a[0]=='1':
    #     print(17)
    #     return
    # if a[0]=='2':
    #     print(23)
    #     return
    # if a[0]=='3':
    #     print(37)
    #     return
    # if a[0]=='4':
    #     print(47)
    #     return
    # if a[0]=='5':
    #     print(53)
    #     return
    # if a[0]=='6':
    #     print(67)
    #     return
    # if a[0]=='7':
    #     print(71)
    #     return
    # if a[0]=='8':
    #     print(83)
    #     return
    # if a[0]=='9':
    #     print(97)
    #     return
    s1 = "abcd"
    s2 = "cdab"
    # print(sorted(s2[::2]))
    d={}
    for i in range(len(s1)):
        d[s1[i]]=i
    d2={}
    for i in range(len(s2)):
        d2[s2[i]]=i
    print(d,d2)
    c=0
    for i in d:
        if abs(d[i]-d2[i])==2:
            c+=1
    print(c)

    
    

for _ in range(int(input())):
   main()