# n=int(input())
# q1,q2=[],[]
# d={}
# for i in range(n):
#     a,b=map(int,input().split())
#     q1.append(a)
#     q2.append(b)
# print(q1)
# print(q2)
# c=0
# for i in range(len(q1)):
#     for j in range(1,len(q1)):
#         print(q1[i],q1[j],q2[i],q2[j])
#         if (q1[i]>q1[j] and q2[i]==q2[j] ) and (q1[i]<q1[j] and q2[i]==q2[j]) and (q1[i]==q1[j] and q2[i]>q2[j]) and (q1[i]==q1[j] and q2[i]<q2[j]):
#             c+=1
# print(c)











#include<bits/stdc++.h>
#define mem(array,num) memset(array,num,sizeof(array))
#define ll long long
# using namespace std;
# int main()
# {
#     ll i,j,n,l,r,u,d,x,y;
#     while(cin>>n)
#     {
#         ll X[n+1],Y[n+1];
#         for(i=0;i<n;i++){
#             cin>>X[i]>>Y[i];
#         }
#         ll point=0;
#         for(i=0;i<n;i++){
#             l=r=u=d=0;
#             x=X[i];y=Y[i];
#             for(j=0;j<n;j++){
#                 if(X[j]==x){
#                     if(Y[j]>y)u++;
#                     if(Y[j]<y)d++;
#                 }
#                 if(Y[j]==y){
#                     if(X[j]>x)r++;
#                     if(X[j]<x)l++;
#                 }
#                 //cout<<l<<" "<<r<<" "<<u<<" "<<d<<"\n";
#             }
#             if(l>0 && r>0 && d>0 && u>0)
#                 point++;
#         }
#         cout<<point<<endl;
#     }
#     return 0;
# }
# point (x', y') is (x, y)'s right neighbor, if x' > x and y' = y
# point (x', y') is (x, y)'s left neighbor, if x' < x and y' = y
# point (x', y') is (x, y)'s lower neighbor, if x' = x and y' < y
# point (x', y') is (x, y)'s upper neighbor, if x' = x and y' > y