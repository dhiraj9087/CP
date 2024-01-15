

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=list(map(int,input().split()))

# if 1 in a:
#     z=a.index(1)
#     if z==4 or z==0:
#         print(4)
#     elif z==3 or z==1:
#         print(3)
#     else:
#         print(2)
# elif 1 in b:
#     z=b.index(1)
#     if z==4 or z==0:
#         print(3)
#     elif z==3 or z==1:
#         print(2)
#     else:
#         print(1)
# elif 1 in c:
#     z=c.index(1)
#     if z==4 or z==0:
#         print(2)
#     elif z==3 or z==1:
#         print(1)
#     else:
#         print(0)
# elif 1 in d:
#     z=d.index(1)
#     if z==4 or z==0:
#         print(3)
#     elif z==3 or z==1:
#         print(2)
#     else:
#         print(1)
# elif 1 in e:
#     z=e.index(1)
#     if z==4 or z==0:
#         print(4)
#     elif z==3 or z==1:
#         print(3)
#     else:
#         print(2)
q=[a,b,c,d,e]
# print(q[0][3])
for i in range(0,5):
    for j in range(0,5):
        if q[i][j] == 1:
            # print(q[i][j],i,j)
            f = abs(3 - (i+1))
            g = abs(3 - (j+1))
            # print(p,o)
            ans = f + g

print(ans)





# #include <bits/stdc++.h>
# using namespace std;
 
# int main()
# {
#     int a[6][6];
#     int ans;
#     int p, o;
#     for (int i = 1; i < 6; i++)
#     {
#         for (int j = 1; j < 6; j++)
#         {
#             cin >> a[i][j];
#         }
#     }
 
#     for (int i = 1; i < 6; i++)
#     {
#         for (int j = 1; j < 6; j++)
#         {
#             if (a[i][j] == 1)
#             {
 
#                 p = abs(3 - i);
#                 o = abs(3 - j);
#                 ans = p + o;
#             }
#         }
#     }
#     cout << ans;
# }
