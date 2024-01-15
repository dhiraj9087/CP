n=int(input())
a=list(map(int,input().split()))
q=a.count(100)
w=a.count(200)
# print(q,w)
# if q==0 or w==0:
#     if n%2==0:
#         print("YES")
#     else:
#         print("NO")
# elif q%2==0 and w%2!=0:
#     print("YES")
# else:
#     print("NO")
if q%2==0 and w%2==0:
    print("YES")
elif q%2!=0 and w%2==0:
    print("NO")
elif q%2==0 and w%2!=0:
    if abs(w*2 - q)%2==0 and q>0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


